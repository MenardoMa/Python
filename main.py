#---------------------------------------------------------
# Type de donnée [int, str, bool, float, liste, tuple, set]
#---------------------------------------------------------

#---------------------------------------------------------
# A Noté tout est objet en python, donc chaque structure
# Contient de proprieté et de methode
#---------------------------------------------------------

#---------------------------------------------------------
# type  = verifier le type de variable
# print = affiche les variable
# instance = verifier si un objet c'est une instance d'une class
#---------------------------------------------------------

_bool = False

_integer = -10

_float = 10.32

_chaine = "Je suis une chaine de caratere"

# une difference ici le tableau s'appelle, le liste
_liste = [10, 23, 8, 'chedo', 'moon', True, False]

# set, un objet
_diction = {
    'name' : 'chedo',
    'age'  : 21,
    'sexe' : 'M',
}

"""
isinstance(<objet>, <class>) permet de verifier si un objet c'est une instance d'une classe
"""


#print(_liste[4])

print(isinstance("4", int))