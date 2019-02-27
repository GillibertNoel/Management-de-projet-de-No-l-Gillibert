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
        else:
            self.productionsdesvilles = []
            for y in range(0,nbvilles):
                u=[]
                for i in range(0,nbproduits):
                    u=u.append(uniform(-fourchette,fourchette))
                self.productionsdesvilles=self.productionsdesvilles.append()
            self.nbvilles = nbvilles
            self.nbproduits = nbproduits
    def passeruntour(self):
        pass