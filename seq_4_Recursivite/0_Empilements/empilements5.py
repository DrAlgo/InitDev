from libEmpilements import *

g = ouvrirFenetreEmpilements(800,600)

nbCubesX = g.NB_CUBES_X


#définition d'une fonction récursive
def f0(g, pos):
    """empile un cube sur la position, si possible
    puis appelle pour empiler sur la position suivante"""

    #condition d'arrêt
    if pos >= nbCubesX:
        return

    #sinon
    g.empilerCube(pos,"green")   # empilement
    f0(g, pos + 1)               # appel récursif
    
f0(g,0)


#fin du programme
g.attendreClic()
g.fermerFenetre()

