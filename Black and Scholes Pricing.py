# Pricing d'options européennes avec Black and Scholes

from math import *
import numpy as np
from scipy.stats import norm
import yfinance as yf
from datetime import datetime


# Les paramètres de BS :
#       - Spot
#       - Strike
#       - taux sans risque
#       - temps jusqu'a la date d'exercice de l'option
#       - Loi Normale centrée réduite
#       - Volatilité du sous-jacent


# A modifier selon vos préférences
symbol = "AAPL"
Strike = 185
Taux_sans_risque = 0.05
temps_restant_annee = 90/360
taux_dividende = 0.05 # Prise en compte dividende dans modèle B-S avec div (3 et 4)


# A ne pas modifier
#-------------------------------------------------------------------------------
end_date = datetime.now().strftime('%Y-%m-%d')
data = yf.download(symbol, start="2024-1-1", end=end_date)
close_prices = data['Close']
close_prices_array = np.array(close_prices)
daily_returns = np.log(close_prices_array[1:] / close_prices_array[:-1])

vol = np.std(daily_returns)
Spot = close_prices_array[-1]
#-------------------------------------------------------------------------------


print(f"\nVoici les inputs du modèle : \n  - Symbol : {symbol} \n  - Strike : {Strike} \n  - Spot : {Spot} \n  - Taux sans risque : {Taux_sans_risque} \n  - Temps restant : {temps_restant_annee} ans \n  - Volatilité : {vol} \n  - Taux dividende : {taux_dividende} \n")
      


# 1. CALCUL DU MODELE POUR UN CALL SANS DIV

def call_sans_div(S, K, r, t, sigma) :

    d1 = (log(S/K) + (r + (sigma**2)/2)*t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    price = S * norm.cdf(d1) - (K * exp(-r * t) * norm.cdf(d2))
    
    return price

print(f"Le valeur du CALL sans dividende: {call_sans_div(Spot, Strike, Taux_sans_risque, temps_restant_annee, vol)}")



# 2. CALCUL DU MODELE POUR UN PUT SANS DIV

def put_sans_div(S, K, r, t, sigma) :

    d1 = (log(S/K) + (r + (sigma**2)/2)*t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    price = -S * norm.cdf(-d1) + (K * exp(-r * t) * norm.cdf(-d2))
    
    return price

print(f"Le valeur du PUT sans dividende: {put_sans_div(Spot, Strike, Taux_sans_risque, temps_restant_annee, vol)}")




# CALCUL DE LA VALEUR DES OPTIONS AVEC PRISE EN COMPTE DES DIVIDENDES 


# 3. CALCUL DU MODELE POUR UN CALL AVEC DIV

def call_avec_div(S, K, r, t, q, sigma) :

    d1 = (log(S/K) + (r + (sigma**2)/2)*t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    price = S * exp(-q * t) * norm.cdf(d1) - (K * exp(-r * t) * norm.cdf(d2))
    
    return price

print(f"Le valeur du CALL avec dividende: {call_avec_div(Spot, Strike, Taux_sans_risque, temps_restant_annee, taux_dividende ,vol)}")



# 4. CALCUL DU MODELE POUR UN PUT AVEC DIV

def put_avec_div(S, K, r, t, q, sigma) :

    d1 = (log(S/K) + (r + (sigma**2)/2)*t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    price = -S * exp(-q * t) * norm.cdf(-d1) + (K * exp(-r * t) * norm.cdf(-d2))
    
    return price

print(f"Le valeur du PUT avec dividende: {put_avec_div(Spot, Strike, Taux_sans_risque, temps_restant_annee, taux_dividende ,vol)}")




