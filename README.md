# Option-Pricing-Using-Black-and-Scholes-Model
J'ai programmé un pricer d'options européennes (avec et sans dividendes) en utilisant le modèle de Black-Scholes.

Les lignes 20 à 24 peuvent être modifiées à votre guise afin d'adapter le pricing à vos paramètres. Le reste n'est pas à modifier.

Dans ce code, j'ai fait en sorte :
- d'importer automatiquement la dernière valeur de l'action choisie, c'est-à-dire la valeur de l'action d'aujourd'hui ;
- de calculer automatiquement la volatilité de l'actif.

IMPORTANT : la valeur de "t" est donnée en années. C'est-à-dire que si vous souhaitez détenir l'option sur 50 jours, il vous faudra mettre :
- t = 50/360.

De plus :
- les modèles 1 et 2 donnent la valeur des options sans les dividendes ;
- les modèles 3 et 4 donnent la valeur des options avec les dividendes.


