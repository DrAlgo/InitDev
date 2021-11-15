from tkiteasy import *

class CanevasEmpilements(Canevas):
    """
    Etend le Canevas de tkiteasy en ajoutant l'empilement de cube
    """

    def __init__(self, master, w, h):
        """
        w : largeur en pixels
        h : hauteur en pixels"""
        self.LARGEUR = w
        self.HAUTEUR = h
        self.COTE_CUBES = 80
        self.NB_CUBES_X = int(self.LARGEUR/self.COTE_CUBES)
        self.NB_CUBES_Y = int(self.HAUTEUR/self.COTE_CUBES) - 1
        self.tab_cubes=[[] for i in range(self.NB_CUBES_X)]
        Canevas.__init__(self,master, w,h)
        self.dessinerLigne(0,self.HAUTEUR - self.COTE_CUBES+2, self.LARGEUR, self.HAUTEUR - self.COTE_CUBES+2, "white")
        for i in range(self.NB_CUBES_X):
            self.afficherTexte(str(i),int(self.COTE_CUBES*(0.5+i)), int(self.HAUTEUR-self.COTE_CUBES/2),"white",20)

    def empilerCube(self, pos, couleur):

        if 0 <= pos < self.NB_CUBES_X and len(self.tab_cubes[pos]) < self.NB_CUBES_Y:
            self.tab_cubes[pos].append(couleur)
            c = self.dessinerRectangle(pos*self.COTE_CUBES +1 , 0 , self.COTE_CUBES-1, self.COTE_CUBES-1, couleur)
            self.actualiser()
            self.pause(.2)

            step = 5 
            yfinal = self.HAUTEUR - (1 + len(self.tab_cubes[pos]))*self.COTE_CUBES
            while c.y < yfinal:
                self.deplacer(c,0,step)
                self.pause(0.0003*step)
                self.actualiser()


def ouvrirFenetreEmpilements(w=800, h=600):
    racine = tk.Tk()
    g = CanevasEmpilements(racine, w, h)
    return g
