import numpy as np
from random import uniform
class World(object):
    """Worlds are currently a set of cities producing varied products at rates chosen randomly at start"""
    def __init__(self, nbvilles = 0, nbproduits = 0, grille = [], fourchette = 0.5) -> None:
        self.villes = np.arange(0, nbvilles, 1)
        estunegrille=True
        nbvillesconsistant = -1
        nbproduitscompteur = 0
        nbproduitsconsistant = 0
        try:
            estuniterable = iter(grille)
        except TypeError as te:
            estunegrille = False
        if estunegrille:
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
        
        if estunegrille:
            self.nbvilles=nbvillesconsistant
            self.nbproduits=nbproduitsconsistant
            self.productionsdesvilles=grille
            self.quantitesproduits=[]
            for y in range(0,self.nbvilles):
                u=[]
                for i in range(0,self.nbproduits):
                    u=u.append(0.0)
                self.quantitesproduits=self.quantitesproduits.append(u)
        else:
            self.productionsdesvilles = []
            self.quantitesproduits=[]
            for y in range(0,nbvilles):
                u=[]#une liste des productions des preduits d'une ville
                b=[]#une liste des quantité des preduits dans une ville
                for i in range(0,nbproduits):
                    u=u.append(uniform(-fourchette,fourchette))
                    b=b.append(0.0)
                self.productionsdesvilles=self.productionsdesvilles.append(u)
                self.quantitesproduits=self.quantitesproduits.append(b)
            self.nbvilles = nbvilles
            self.nbproduits = nbproduits
    def passeruntour(self):
        for i in self.villes:
            for y in range(0,self.nbproduits):
                self.quantitesproduits[i][y]=self.productionsdesvilles[i][y]+self.quantitesproduits[i][y]