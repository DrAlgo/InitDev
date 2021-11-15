from libEmpilements import *

g = ouvrirFenetreEmpilements(800,600)

nbCubesX = g.NB_CUBES_X


#définition d'une fonction récursive
def f0(g, pos):

    g.empilerCube(pos,"green")

    #appel récursif ! (on teste pour ne pas sortir)
    if pos + 1 < nbCubesX:
        f0(g, pos + 1)
    
f0(g,0)


#fin du programme
g.attendreClic()
g.fermerFenetre()

