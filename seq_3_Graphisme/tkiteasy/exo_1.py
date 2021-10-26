#coding: utf-8
from tkiteasy import *


# ouverture de fenêtre
g = ouvrirFenetre(800,600)

# votre programme ICI

# boucle à vide qui attend un clic
while g.recupererClic() == None:
    continue

# fermeture fenêtre
g.fermerFenetre()
