
#Nous allons ecrire des instructions et cela sera interpreter par un interpreteur
"""
Une instruction c'est une ligne de code ou un ordre qu'on donne pour que notre programme face la chose 
comme on le souhaite
"""


"""
Les variables : 
C'est une case memoire qui permet de sauvegarder les informations temporairement en memoire
avec python nous avons plusieur type de donnée en sauvegarder

Le langage python utilise un typage dynamique,

Une variable dois avoir un :
                        nom, 
                        pas de caractere special, 
                        toujour commencer par une lettre,
                        ne dois pas contenir des espaces

Types de données standars : (Entier (int), Decimal (float), Chaine de caractere (str), Booleen (bool))

Le fonction type, retourne le type d'une chaine

En ce qui concerne le variable flotant, decimal (nous devons toujour le separere avec un .)

=> Pour afficher une variable ou va utiliser la fonction (print), 
=> Pour verifier le type d'une variable on va utiliser la methode (type)

=> En python tout est objet, donc chaque variable ou type est lie a de methode et proprieté

"""

_age = 10
_sexe = "M"
decimal_variable = 10.25

_bool_true = True
_bool_false = False

_val_a = "Moon"
_val_b = "Emie"

chaine = "Je suis une chaine de caractere"

#print(type(_age), type(_sexe), type(decimal_variable))
#Nous allons utiliser un f string pour injecté les variable (faire l'interpolation)

text = f"Je suis une {_val_a} et j'ai une femme qui s'appelle {_val_b}"

print(text)