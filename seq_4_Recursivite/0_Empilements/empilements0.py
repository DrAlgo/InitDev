from libEmpilements import *

#on ouvre un objet graphique, version de la lib Empilements
g = ouvrirFenetreEmpilements(800,600)


g.attendreClic()
g.empilerCube(0, "green")

g.attendreClic()
g.empilerCube(2, "blue")

g.attendreClic()
#on peut en empiler plusieurs !
g.empilerCube(5, "yellow")
g.empilerCube(6, "cyan")
g.empilerCube(5, "magenta")

g.attendreClic()
g.empilerCube(9, "red")


#fin du programme
g.attendreClic()
g.fermerFenetre()
