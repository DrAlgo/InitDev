from libEmpilements import *

g = ouvrirFenetreEmpilements(800,600)



#on définit trois fonctions
def f0(g,pos):
    g.empilerCube(pos, "green")
    g.attendreClic()
    f1(g, pos+1)

def f1(g,pos):
    f2(g, pos -1)
    g.attendreClic()
    g.empilerCube(pos, "yellow")
    g.attendreClic()
    f2(g,pos+1)

def f2(g, pos):
    g.empilerCube(pos+2, "blue")

#on lance la fonction f1
f0(g, 2)


#fin du programme
g.attendreClic()
g.fermerFenetre()
