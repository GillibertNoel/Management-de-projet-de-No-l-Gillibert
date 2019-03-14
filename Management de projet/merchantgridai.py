from merchantbehaviour import MerchantBehaviour
from random import uniform
def foncajustementpardefaut(valeur,perteougain):
    if perteougain<0:
        return max(valeur/2,0.05)
    if perteougain>0:
        return valeur+1
    return valeur
    
#cette ia prends plus souvent un chemin s'il rapporte et moins souvent un chemin s'il ne rapporte pas
class MerchantGridAI(MerchantBehaviour):
    def __init__(self,world,fonctionperteougain = foncajustementpardefaut) -> None:
        super().__init__()
        self.fonctionperteougain=fonctionperteougain
        self.grille=[] #de forme: villes , villes , produits
        for y in range(0,world.nbvilles):
            u=[]
            for z in range(0,world.nbvilles):
                w=[]
                for i in range(0,world.nbproduits):
                    if z==y:
                        w.append(0.0)
                    else:
                        w.append(1.0)
                u.append(w)
            self.grille.append(u)
    def echecoureussite(self,transaction,perteougain):#une valeur negative de perteougain indique une perte et une valeur positive indique un gain
        self.grille[transaction[0]][transaction[1]][transaction[2]]=self.fonctionperteougain(self.grille[transaction[0]][transaction[1]][transaction[2]],perteougain)
    def choisirchemin(self,position):#doit renvoyer un triplet ville1,ville2,produit
        #l'on choisit une destination
        sumsury=0
        y=[]
        for i in self.grille[position]:
            u=0
            for j in i:
                u=u+j
            sumsury=sumsury+u
            y.append(u)
        z=uniform(0,sumsury)
        destination=0
        for i in y:
            z=z-i
            if z<0:
                break
            destination = destination + 1
        # choix du produit
        print(destination)
        z=uniform(0,y[destination])
        produitchoisit = 0
        for i in self.grille[position][destination]:
            z=z-i
            if z<0:
                break
            produitchoisit=produitchoisit+1
        return [position,destination,produitchoisit]
        