from libGrille import *

#on ouvre un objet graphique, version de la lib Grille
g = ouvrirFenetreGrille(80,16,12)

#on place des murs
for i,j in [(2,0),(2,1),(2,2),(3,3),(4,3),(4,4),(5,4),(5,5),(5,6),(4,7),(4,8),(3,9),(2,8),(1,7),(0,7),
    (10,6),(11,7),(10,8),(9,7)] :
    g.changerCarre(i,j,"black")

#démo de l'API

#0) changer carré : démo ci-dessus pour placer les murs

#1) on fait apparaitre pacman et on le déplace sauvagement
g.placer_pacman(4,2)
g.pause(1)
g.placer_pacman(10,4)
g.pause(1)
g.placer_pacman(3,10)
g.pause(1)

#2) case valide : une case qui est bien dans la grille et n'est pas un mur (couleur noire)

print(g.case_valide(2,2)) # faux en principe
print(g.case_valide(3,2)) # vrai en principe
print(g.case_valide(30,-200)) # faux en principe

g.pause(1)

#3) mettre une flèche rouge entre deux cases, puis la supprimer
f = g.dessinerFleche(13,5,13,6)
g.pause(1)
g.supprimer(f)
g.pause(1)

#4) changer une case en bleu, et obtenir la couleur d'une case
g.changerCarre(7,7,"blue")
print(g.getCouleur(7,7))


#fin du programme
g.attendreClic()
g.fermerFenetre()