from tkiteasy import *

class CanevasGrille(Canevas):
    """
    Etend le Canevas de tkiteasy en ajoutant les fonctionnalités de la grille
    """

    def __init__(self, master, cote, nb_carres_x, nb_carres_y):
        """
        w : largeur en pixels
        h : hauteur en pixels"""
        self.LARGEUR = nb_carres_x*cote
        self.HAUTEUR = nb_carres_y*cote
        self.COTE_CARRE = cote
        self.NB_CARRES_X = nb_carres_x
        self.NB_CARRES_Y = nb_carres_y
        d = int(self.COTE_CARRE/10) #separation des carres
        Canevas.__init__(self,master, self.LARGEUR+d,self.HAUTEUR+d)

        self.carres = [[None]*self.NB_CARRES_Y for i in range(self.NB_CARRES_X)]

        for i in range(self.NB_CARRES_X):
            for j in range(self.NB_CARRES_Y):
                self.carres[i][j] = self.dessinerRectangle(d + i*self.COTE_CARRE, d + j*self.COTE_CARRE, self.COTE_CARRE-d, self.COTE_CARRE-d, "gray")

        self.col_carres = [["gray"]*self.NB_CARRES_Y for i in range(self.NB_CARRES_X)]
        self.pacman_pos = None
        self.pacman_h = None

    def changerCarre(self,i,j,col):
        """
        change la couleur du carré (i,j)
        """
        self.changerCouleur(self.carres[i][j], col)
        self.col_carres[i][j] = col

    def dessinerFleche(self, i1, j1, i2, j2):
        """
        dessine une fleche qui part du carré i1,j1 jusqu'au carré i2,j2
        """
        d = int(self.COTE_CARRE/10) #separation des carres
        x1 = int(d + (i1+0.5)*self.COTE_CARRE)
        y1 = int(d + (j1+0.5)*self.COTE_CARRE)
        x2 = int(d + (i2+0.5)*self.COTE_CARRE)
        y2 = int(d + (j2+0.5)*self.COTE_CARRE)
        l = self.create_line(x1,y1,x2,y2,fill="red",arrow="last", width=5, arrowshape=(20,20,5))
        return ObjetGraphique(l, x1, y1, "red")




    def getCouleur(self, i,j):
        """
        renvoie la couleur du carré (i,j)
        """
        return self.col_carres[i][j]

    def placer_pacman(self,i,j):
        pos_x = int((i+0.5)*self.COTE_CARRE-15) 
        pos_y = int((j+0.5)*self.COTE_CARRE-15) 
        if self.pacman_pos == None:
            self.pacman_h = self.afficherImage(pos_x, pos_y, "pacman.png")
        else:
            self.deplacer(self.pacman_h, pos_x - self.pacman_h.x,  pos_y - self.pacman_h.y)
        self.pacman_pos = (i,j)
        self.actualiser()

    def case_valide(self,i,j):
        return (0 <= i < self.NB_CARRES_X) and (0 <= j < self.NB_CARRES_Y) and self.col_carres[i][j] != "black"

def ouvrirFenetreGrille(cote = 50, nb_carres_x=16, nb_carres_y=12):
    racine = tk.Tk()
    g = CanevasGrille(racine, cote, nb_carres_x, nb_carres_y)
    return g
