from libGrille import *

#on ouvre un objet graphique, version de la lib Grille
g = ouvrirFenetreGrille(80,16,12)

#on place des murs
for i,j in [(2,0),(2,1),(2,2),(3,3),(4,3),(4,4),(5,4),(5,5),(5,6),(4,7),(4,8),(3,9),(2,8),(1,7),(0,7),
    (10,6),(11,7),(10,8),(9,7),(8,7),(6,7),(6,0),(6,1),(15,3),(14,3),(12,0),(12,1),(12,2)] :
    g.changerCarre(i,j,"black")


def exploration(i,j):
    """Démarre l'exploration de la case de coordonnées (i,j)
    Cette case est censée être valide et inexplorée (grise). L'exploration consiste en :
    - changer la case en bleu pour marquer le fait qu'elle est exklorée
    - déplacer pacman sur cette case
    - tester chacune des 4 cases voisines, et si cette case est valide et inexplorée, on appelle la fonction exploration dessus
    - quand une de ces explorations est terminée, on peut remettre pacman en i,j 
    - en dernière amélioration, on peut placer une flèche entre cette case et la case voisine si une exploration est lancée,
    et supprimer la flèche quand de la case voisine est est terminée
    """

    g.changerCarre(i,j,"blue")
    g.placer_pacman(i,j)
    # a completer...


g.attendreClic()
exploration(7,5)


#fin du programme
g.attendreClic()
g.fermerFenetre()

