from libEmpilements import *

g = ouvrirFenetreEmpilements(800,600)



#on définit trois fonctions
def fa(g,pos):
    fb(g, pos+1)
    g.empilerCube(pos, "green")
    g.attendreClic()
    fb(g, pos)

def fb(g,pos):
    fc(g, pos)
    g.attendreClic()
    g.empilerCube(pos, "yellow")

def fc(g, pos):
    g.empilerCube(pos+2, "blue")
    g.attendreClic()



#fin du programme
g.attendreClic()
g.fermerFenetre()

