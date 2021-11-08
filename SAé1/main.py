#coding: utf-8
from libgrapythk import *
import random
import matplotlib.pyplot as pyplt

#DEFINES ###################################################################
SIZECASE=15 # taille d'une case en pixels
NBCASES=30  # nb de cases

#PROIES
REPRO=True # est-ce que deux proies qui se touchent se reproduisent?
FBIRTHPROIE = 1 # fréquence d'apparition des proies  (nb tours)
LIFEPROIE = 40  # durée de vie max d'une proie
NBPROIES_START = 40 # nombre de proies introduites au lancement

#PREDATEURS
LIFEPRED = 60 # durée de vie max d'un prédateur
NRJPRED = 15  # énergie de départ d'un prédateur (-1 par tour)
NRJBIRTH = 20 # énergie requise pour se reproduire
NRJMIAM =  6  # énergie obtenue en mangeant
NBPRED_START = 20 # nombre de prédateurs introduits au lancement
DISTFLAIR = 15 # distance à laquelle le prédateur sent la proie

"""Conditions générant de beaux cycles
#PROIES
REPRO=True # est-ce que deux proies qui se touchent se reproduisent?
FBIRTHPROIE = 1 # fréquence d'apparition des proies  (nb tours)
LIFEPROIE = 40  # durée de vie max d'une proie
NBPROIES_START = 40 # nombre de proies introduites au lancement

#PREDATEURS
LIFEPRED = 60 # durée de vie max d'un prédateur
NRJPRED = 15  # énergie de départ d'un prédateur (-1 par tour)
NRJBIRTH = 20 # énergie requise pour se reproduire
NRJMIAM =  6  # énergie obtenue en mangeant
NBPRED_START = 20 # nombre de prédateurs introduits au lancement
DISTFLAIR = 15 # distance à laquelle le prédateur sent la proie
"""

"""Conditions stables petite population proies sans pred et sans repro
REPRO=False
SIZECASE=20
NBCASES=30
FBIRTHPROIE = 5
LIFEPROIE = 40
NBPROIES_START = 10"""

################################################################################
# plusTuple
################################################################################
def plusTuple(t,u):
    return((t[0]+u[0],t[1]+u[1]))

################################################################################
# dessinerTerrain
################################################################################
def dessinerTerrain():
    for x in range(SIZECASE,SIZECASE*NBCASES,SIZECASE):
        g.dessiner_ligne(x,0,x,SIZECASE*NBCASES,"grey")

    for y in range(SIZECASE,SIZECASE*NBCASES,SIZECASE):
        g.dessiner_ligne(0,y,SIZECASE*NBCASES,y,"grey")

################################################################################
# dessiner
################################################################################
def dessiner(c,qui):
    z = tab2grafx(c)
    if qui == "pred":
        color = "red"
    else:
        color = "green"
    return g.dessiner_disque(z[0]+SIZECASE/2,z[1]+SIZECASE/2,SIZECASE/3,color)

################################################################################
# tab2grafx
################################################################################
def tab2grafx(c):
#     print (f"{c} => ({c[0]*SIZECASE},{c[1]*SIZECASE})")
    return (c[0]*SIZECASE,c[1]*SIZECASE)

################################################################################
# naissanceProie
################################################################################
def naissanceProie(proies_age, proies_objgfx, carte, pos=None):
    if pos:
        c,l = pos[0],pos[1]
    else:
        c = random.randint(0,NBCASES-1)
        l = random.randint(0,NBCASES-1)

    if (c,l) not in carte:
        o = dessiner((c,l),"proie")
        proies_age[(c,l)]  = LIFEPROIE
        proies_objgfx[(c,l)]  = o
        carte[(c,l)] = o # à revoir?
#         print(f"Proie {(c,l)} is born")
    return (c,l)

################################################################################
# naissancePred
################################################################################
def naissancePred(pred_age, pred_objgfx, pred_nrj, carte):
    c = random.randint(0,NBCASES-1)
    l = random.randint(0,NBCASES-1)

    if (c,l) not in carte:
        o = dessiner((c,l),"pred")
        pred_age[(c,l)] = LIFEPRED
        pred_nrj[(c,l)] = NRJPRED
        pred_objgfx[(c,l)]  = o
        carte[(c,l)] = o # à revoir?
#         print(f"Pred {(c,l)} is born")
    return (c,l)

################################################################################
# voisinage
################################################################################
def voisinage(c,carte, proies_age):
#     print("voisinage",c)
    vois = set([(-1,0),(1,0),(0,-1),(0,1)])
    if c[0]==0:
        vois.discard((-1,0))
    elif c[0]==NBCASES-1:
        vois.discard((1,0))

    if c[1]==0:
        vois.discard((0,-1))
    elif c[1]==NBCASES-1:
        vois.discard((0,1))

    vois2 = set()
    repro = False
    for v in vois:
        if plusTuple(c,v) not in carte:
            vois2.add(v)
        elif plusTuple(c,v) in proies_age:
            repro = True
#     print("vois possible",vois2,"repro",repro)
                    
    if not vois2:
        return None, None
    birth = None
    if REPRO and repro and len(vois2)>1:
        birth = random.choice(list(vois2))
#         print("birth sur",birth)
        vois2.discard(birth)
    move = random.choice(list(vois2))
#     print("move sur",move)
    return move,birth

################################################################################
# distance
################################################################################
def distance(a,b):
    return abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2

################################################################################
# hunt
################################################################################
def hunt(c,carte,proies_age):
#     print("hunt",c)
    vois = set([(-1,0),(-1,-1),(-1,1),(1,-1),(1,1),(1,0),(0,-1),(0,1)])
    if c[0]==0:
        vois.discard((-1,0)); vois.discard((-1,1)); vois.discard((-1,-1))
    elif c[0]==NBCASES-1:
        vois.discard((1,0)); vois.discard((1,-1)); vois.discard((1,1))

    if c[1]==0:
        vois.discard((0,-1)); vois.discard((1,-1)); vois.discard((-1,-1))
    elif c[1]==NBCASES-1:
        vois.discard((0,1)); vois.discard((-1,1)); vois.discard((1,1))

    vois2 = set()
    for v in vois:
        if plusTuple(c,v) in proies_age:
#             print("miam vers",v)
            return v, True
        
        if plusTuple(c,v) not in carte:
            vois2.add(v)
#     print("vois",vois2)
                    
    if not vois2:
        return None, False

    plusProcheProie = NBCASES**2*2
    bestVois = None
    for v in vois2:
        for p in proies_age:
#             if v[0]*p[0]>=0 or v[1]*p[1]>=0: #optim?
                dist = distance(plusTuple(c,v),p)
                if dist<DISTFLAIR**2 and dist < plusProcheProie:
                    plusProcheProie = dist
                    bestVois = v
#     print("move vers",bestVois)
    if bestVois == None:
        bestVois = random.choice(list(vois2))
    return bestVois, False

################################################################################
# life
################################################################################
def life(pred_age, pred_objgfx, pred_nrj, proies_age, proies_objgfx, carte):
#     print(f"PRED AVANT {len(pred_age)} {len(pred_objgfx)} {len(pred_nrj)}")
#     print(f"PROIES AVANT {len(proies_age)} {len(proies_objgfx)}")
#     print(f"CARTE AVANT {len(carte)}")
#     print(f"pred_age entrée: {pred_age}")
#     print(f"pred_nrj entrée: {pred_nrj}")
    npred_age = dict(pred_age)
    for c in pred_age:
#         print(f"PRED allons-y pour {c}")
        npred_age[c] -= 1 # on diminue l'âge
        pred_nrj[c] -= 1 # et l'énergie
        if npred_age[c]==0 or pred_nrj[c]==0: # si dead
            if pred_nrj[c]!=0:
#                 print("PRED DEAD DE FAIM!!",c)
#             else:
                print("PRED DEAD de vieillesse!!",c)
            g.supprimer(pred_objgfx[c])
            npred_age.pop(c)
            pred_objgfx.pop(c)
            pred_nrj.pop(c)
            carte.pop(c)
        else:
#             print("not dead")
            move,eat = hunt(c, carte, proies_age)
            if move:
#                 print(f"PRED {c} bouge de {move}: {plusTuple(c,move)}")
                nextpos = plusTuple(move,c)
                if eat:
#                     print("MIAM!!",nextpos)
                    g.supprimer(proies_objgfx[nextpos])
                    proies_age.pop(nextpos)
                    proies_objgfx.pop(nextpos)
                    carte.pop(nextpos)
                    pred_nrj[c] += NRJMIAM
                    if pred_nrj[c] >= NRJBIRTH:
                        i=naissancePred(npred_age, pred_objgfx, pred_nrj, carte)
#                         print("BIRTHPRED!!",i)
            
                g.deplacer(pred_objgfx[c],move[0]*SIZECASE,move[1]*SIZECASE)
                pred_objgfx[nextpos] = pred_objgfx[c]
                pred_objgfx.pop(c)
                pred_nrj[nextpos] = pred_nrj[c]
                pred_nrj.pop(c)
                carte[nextpos] = carte[c]
                carte.pop(c)
                npred_age[nextpos] = pred_age[c]
                npred_age.pop(c)

#     print(f"PRED MILIEU {len(npred_age)} {len(pred_objgfx)} {len(pred_nrj)}")
#     print(f"PROIES MILIEU {len(proies_age)} {len(proies_objgfx)}")
#     print(f"CARTE MILIEU {len(carte)}")
#     print("npred_age:",npred_age.keys())
#     print("proies_age:",proies_age.keys())
#     print("carte:",carte.keys())
#     print(f"proies_age entrée: {proies_age}")
    nproies_age = dict(proies_age)
    for c in proies_age:
#         print(f"PROIES allons-y pour {c}")
        proies_age[c] = proies_age[c]-1 # on diminue l'âge
        if proies_age[c] == 0: # si dead
            print("DEAD!!",c)
            g.supprimer(proies_objgfx[c])
            nproies_age.pop(c)
            proies_objgfx.pop(c)
            carte.pop(c)
        else:
#             print("not dead")
            move,repro = voisinage(c, carte, nproies_age)
            if repro:
#                 print("NAISSANCE!",plusTuple(repro,c))
                naissanceProie(nproies_age, proies_objgfx, carte, plusTuple(c,repro))
#                 input()
            if move:
#                 print(f"PROIE {c} bouge de {move}: {plusTuple(c,move)}")
                nextpos = plusTuple(move,c)
                g.deplacer(proies_objgfx[c],move[0]*SIZECASE,move[1]*SIZECASE)
                proies_objgfx[nextpos] = proies_objgfx[c]
                proies_objgfx.pop(c)
                try:
                    carte[nextpos] = carte[c]
                except KeyError:
#                     print("carte:",carte.keys())
#                     print(f"nextpos:{nextpos}, c:{c}")
                    input()
                carte.pop(c)
                nproies_age[nextpos] = proies_age[c]
                nproies_age.pop(c)
#     print(f"PRED APRES {len(npred_age)} {len(pred_objgfx)} {len(pred_nrj)}")
#     print(f"PROIES APRES {len(nproies_age)} {len(proies_objgfx)}")
#     print(f"CARTE APRES {len(carte)}")
        
    g.update()
    return npred_age, nproies_age


################################################################################
# MAIN #########################################################################
################################################################################
# ouverture de fenêtre
g = ouvrir_fenetre(SIZECASE*NBCASES,SIZECASE*NBCASES)
dessinerTerrain()
g.update()

proies_age = {} # dico des âges de proies
proies_objgfx = {} # dico des objets graphiques liés aux proies
proies_eff = [] # effectifs des proies
pred_age = {} # dico des âges de prédateurs
pred_nrj = {} # dico des énergies de prédateurs
pred_objgfx = {} # dico des objets graphiques liés aux prédateurs
pred_eff = [] # effectifs des prédateurs
carte = {} # dico des objets graphiques des cases

tour = 0
maxtours = int(input("Combien de tours? "))
while tour<maxtours:
#     print("Tour ",tour)
# NAISSANCE PROIE
    if tour<NBPROIES_START or (FBIRTHPROIE and tour%FBIRTHPROIE==0):
        naissanceProie(proies_age, proies_objgfx, carte)
        g.update()
    if tour<NBPRED_START:
        naissancePred(pred_age, pred_objgfx, pred_nrj, carte)
        g.update()
    tour += 1

    pred_age, proies_age = life(pred_age, pred_objgfx, pred_nrj, proies_age, proies_objgfx, carte)
    g.pause(.1)
    proies_eff.append(len(proies_age))
    pred_eff.append(len(pred_age))
        
pyplt.plot(range(maxtours), proies_eff, color="green")
pyplt.plot(range(maxtours), pred_eff, color="red")
pyplt.show()
# fermeture fenêtre
input("fermer-fenetre - presser ENTREE")
g.fermer_fenetre()
