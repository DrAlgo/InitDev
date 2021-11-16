from libGrille import *

#on ouvre un objet graphique, version de la lib Grille
g = ouvrirFenetreGrille(80,16,12)

#on place des murs
for i,j in [(2,0),(2,1),(2,2),(3,3),(4,3),(4,4),(5,4),(5,5),(5,6),(4,7),(4,8),(3,9),(2,8),(1,7),(0,7),
    (10,6),(11,7),(10,8),(9,7)] :
    g.changer_carre(i,j,"black")

#une case est accessible si elle est dans la grille et n'est pas un mur (couleur noire)

#on fait avancer pacman jusqu'à un mur
#et on garde sa trace en bleu
i,j = 9,2

while g.case_valide(i,j):
    g.changer_carre(i,j,"blue")
    g.placer_pacman(i,j)
    g.pause(0.5)
    i -= 1
    j += 1

#fin du programme
g.attendreClic()
g.fermerFenetre()
