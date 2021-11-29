#coding: utf-8
from time import time                   # fonction permettant de mesurer le temps
import matplotlib.pyplot as pyplt       # module de créatio de graphiques
from random import shuffle              # fonction de mélange d'une liste
from math import sin                    # un petit coup de trigo


################################################################################
# Exercice 0
################################################################################
def randlist(n):
    ''' Construit une liste de n entiers compris entre 0 et n-1, et répartis aléatoirement.
    Entrée: n entier >0
    Sortie: liste d'entiers '''
    pass

################################################################################
# Exercice 1
################################################################################
def test_randlist():
    ''' Fonction de test de randlist'''
    pass

################################################################################
# Exercice 3
################################################################################
def tri_sel(l):
    ''' Tri une liste d'entiers quelconques en ordre croissant par l'algorithme du tri par sélection
    Entrée: l liste d'entiers
    Sorti: liste d'entiers triés '''
    pass

################################################################################
# Exercice 4
################################################################################
def test_tri_sel():
    pass


################################################################################
# Exercice 6
################################################################################
def tri_bul(l):
    ''' Tri une liste d'entiers quelconques en ordre croissant par l'algorithme du tri à bulles
    Entrée: l liste d'entiers
    Sortie: liste d'entiers triés '''
    pass

################################################################################
# Exercice 7
################################################################################
def test_tri_bul():
    pass

            
################################################################################
# Exercice 8
################################################################################
def perf_reverse(n):
    l = list(range(n))  # construction d'une liste de n entiers
    debut = time()      # on stocke le temps au démarrage de notre action
    l.reverse()         # ICI, on mesure le temps requis pour effecter ce reverse()
    fin = time()        # on stocke le temps à la fin de l'action
    print("reverse de",n,"entiers:",fin-debut)  # on peut ensuite facilement obtenir
                                                # le temps écoulé entre fin et début

################################################################################
# Exercice 10
################################################################################
def demo_pyplot():
# PREMIER AFFICHAGE: LES PUISSANCES DE 2
    ly = [ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024] # 2**n pour n allant de 0 à 10
    lx = [ 0, 1, 2, 3, 4,  5,  6,  7,   8,   9,   10]   # 0 à 10
    pyplt.plot(lx, ly, "blue")  # traçage du graphique
    pyplt.show()                # affichage de la fenêtre

# DEUXIEME AFFICHAGE: UN SINUS
    ly2 = [ sin(x/10)*1000 for x in range(60) ]  # ly2 est une liste contenant 
            # sin(0)*1000, sin(0.1)*1000, sin(0.2)*1000,...,sin(5.9)*1000
    lx2 = [ x/10 for x in range(60) ]         # lx2 est la liste des abscisses employées:
            # 0.1, 0.2, 0.3,...,5.9
    pyplt.plot(lx2, ly2, "red")   # on passe à plot la liste des abscisses et des ordonnées des points à tracer
    pyplt.plot(lx, ly, "blue")  # on ajoute le premier graphique
    pyplt.show()                # on trace les deux courbes


