from libEmpilements import *

g = ouvrirFenetreEmpilements(800,600)



#on définit trois fonctions
def fA(g,pos):
    g.empilerCube(pos, "white")
    g.attendreClic()
    fB(g, pos-1)
    g.empilerCube(pos+1, "green")
    g.attendreClic()
    fB(g, pos+1)
    g.empilerCube(pos+2, "blue")
    g.attendreClic()

def fB(g,pos):
    g.empilerCube(pos, "yellow")
    g.empilerCube(pos+1, "yellow")
    g.attendreClic()


#fin du programme
g.attendreClic()
g.fermerFenetre()
