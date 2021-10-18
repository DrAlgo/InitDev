#coding: utf-8
from libgrapythk import *


# ouverture de fenêtre
g = ouvrirFenetre(800,600)

# afficher image
pacman = g.afficherImage(400,300,"./pacman.png")

# deplacement
input("fonction deplacer - presser ENTREE")
for i in range(100):
   g.deplacer(pacman,0,-1)
   g.update()
   g.pause()

# affichage coordonnées
print("coordonnées pacman.x",pacman.x, 'pacman.y',pacman.y)

# interaction souris clavier
input("fonctions recuperer_touche & recuperer_clic - presser ENTREE (jouer avec les flèches ou la souris, q pour quitter)")
while(True):
    touche = g.recupererTouche()
    clic = g.recupererClic()
    if touche=="q":
        break
    elif touche=="Right" and pacman.x<800:
        g.deplacer(pacman,5,0)
    elif touche=="Left" and pacman.x>=5:
        g.deplacer(pacman,-5,0)
    elif touche=="Up" and pacman.y>=5:
        g.deplacer(pacman,0,-5)
    elif touche=="Down"and pacman.y<600:
        g.deplacer(pacman,0,5)

    if clic:
        g.deplacer(pacman,clic.x-pacman.x, clic.y-pacman.y)
    g.actualiser()

# fonctions géométriques standard
input("dessiner-disque - presser ENTREE")
d1 = g.dessinerDisque(600,500,30,"grey")
input("dessiner-cercle - presser ENTREE")
g.dessinerCercle(100,500,30,"purple")
input("dessiner-ligne - presser ENTREE")
g.dessinerLigne(200,20,750,340,"pink")
input("changer-pixel - presser ENTREE")
g.changerPixel(190,20,"white")
input("changer-pixel - presser ENTREE")
g.changerPixel(191,20,"red")
input("changer-pixel - presser ENTREE")
g.changerPixel(191,21,"yellow")
input("changer-pixel - presser ENTREE")
g.changerPixel(190,21,"green")
input("dessiner-rectangle - presser ENTREE")
r1 = g.dessinerRectangle(699,499,100,50,"yellow")
r2 = g.dessinerRectangle(442,416,40,80,"green")
input("supprimer - presser ENTREE")
g.supprimer(r2)
input("afficher-texte - presser ENTREE")
t1 = g.afficherTexte("coucou",200,200,"red")
input("afficher-texte size 30- presser ENTREE")
g.afficherTexte("coucou",400,300,"red", 30)

# modifications objets existants
input("changer-texte - presser ENTREE")
g.changerTexte(t1,"ouais")
input("changer-couleur - presser ENTREE")
g.changerCouleur(t1,"blue")
input("changer-couleur - presser ENTREE")
g.changerCouleur(r1,"blue")


# fermeture fenêtre
input("fermer-fenetre - presser ENTREE")
g.fermerFenetre()
input("fin du programme - presser ENTREE")
