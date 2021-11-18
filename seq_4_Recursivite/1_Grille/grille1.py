from libGrille import *

#on ouvre un objet graphique, version de la lib Grille
g = ouvrirFenetreGrille(80,16,12)

#on place des murs
for i,j in [(2,0),(2,1),(2,2),(3,3),(4,3),(4,4),(5,4),(5,5),(5,6),(4,7),(4,8),(3,9),(2,8),(1,7),(0,7),
    (10,6),(11,7),(10,8),(9,7),(8,7),(6,7),(6,0),(6,1),(15,3),(14,3),(12,0),(12,1),(12,2)] :
    g.changer_carre(i,j,"black")


def explorer(i,j):
    g.changer_carre(i,j,"cyan")
    g.actualiser()
    g.pause(0.1)
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        i1,j1 = i+dx, j+dy
        if g.case_valide(i1,j1) and g.get_couleur(i1,j1) != "cyan":
            f = g.dessinerFleche(i,j,i1,j1)
            explorer(i1,j1)
            g.supprimer(f)
            g.actualiser()
            g.pause(0.1)

explorer(7,5)

#g.dessinerFleche(i,j,i+1,j)
#g.dessinerFleche(5,5,6,6)
#g.dessinerFleche(7,7,7,8)

#fin du programme
g.attendreClic()
g.fermerFenetre()

