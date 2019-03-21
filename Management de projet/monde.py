# coding: utf-8
import numpy as np
from random import uniform
def evalcout(nombreduproduit):
    if nombreduproduit>0.01:
        return min(max((1/nombreduproduit)*10,5),1)
    return 5
class World(object):
    """Worlds are currently a set of cities producing varied products at rates chosen randomly at start"""
    def __init__(self, nbvilles = 0, nbproduits = 0, grille = [], fourchette = 0.5,evaluationdecout=evalcout) -> None:
        estunegrille = True
        bool = False
        self.evaluationdecout=evaluationdecout
        nbvillesconsistant = -1
        nbproduitscompteur = 0
        nbproduitsconsistant = 0
        try:#voir si la grille est un vrai truc
            estuniterable = iter(grille)
        except TypeError as te:
            estunegrille = False
        if estunegrille:
            if len(grille)>0:
                bool = True
        if bool:
            for i in grille:
                nbvillesconsistant = nbvillesconsistant + 1
                try:
                    estuniterable = iter(i)
                except TypeError as te:
                    estunegrille = False
                if estunegrille:    
                    nbproduitscompteur = len(i)
                    if nbproduitsconsistant == -1:
                        nbproduitsconsistant = nbproduitscompteur
                    if nbproduitsconsistant != nbproduitscompteur:
                        estunegrille = False
                
                    for j in i:
                        if not j.isdecimal():
                            estunegrille = False
                        self.nbvilles=nbvillesconsistant
            self.nbproduits=nbproduitsconsistant
            self.productionsdesvilles=grille
            self.quantitesproduits=[]
            for y in range(0,self.nbvilles):
                u=[]
                for i in range(0,self.nbproduits):
                    u.append(0.0)
                self.quantitesproduits.append(u)
        else:
            self.productionsdesvilles = []
            self.quantitesproduits=[]
            for y in range(0,nbvilles):
                u=[]#une liste des productions des preduits d'une ville
                b=[]#une liste des quantité des preduits dans une ville
                for i in range(0,nbproduits):
                    u.append(uniform(-fourchette,fourchette))
                    b.append(0.0)
                self.productionsdesvilles.append(u)
                self.quantitesproduits.append(b)
            self.nbvilles = nbvilles
            self.nbproduits = nbproduits
    def passeruntour(self):
        for i in range(0,self.nbvilles):
            for y in range(0,self.nbproduits):
                self.quantitesproduits[i][y]=self.productionsdesvilles[i][y]+self.quantitesproduits[i][y]
                
    """verifie si l'on a une unité de produit dans la ville puis consomme s'il y a au
     moins une unité et renvoie "True" sinon cela renvoie False"""
    def prendreproduit(self,produit,ville):
        if self.quantitesproduits[ville][produit]>1:
            self.quantitesproduits[ville][produit] = self.quantitesproduits[ville][produit]-1
            return True
        return False
    def donnerproduit(self,produit,ville):
        self.quantitesproduits[ville][produit] = self.quantitesproduits[ville][produit]+1
        pass
    def evaluercoutproduit(self,produit,ville):
        if ville > self.nbvilles-1:
            print("ville trop grande")
            print(ville)
        if produit > self.nbproduits-1:
            print("produit trop grand")
            print(produit)
        return self.evaluationdecout(self.quantitesproduits[ville][produit])
        pass