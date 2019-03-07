# coding: utf-8
class Merchant(object):
    def __init__(self, villeinit = None, argentinit = 1000, comportementinit = None) -> None:
        self.ville = villeinit
        self.argent = argentinit
        self.comportement = comportementinit
    def choisirtransaction(self):
        self.prochainchemin = self.comportement.choisirchemin(self.ville)
        pass
    """le marchant agit un tour"""
    def passeruntour(self,monde):
        ben = self.effectuertransaction(monde,self.prochainchemin)
        self.comportement.echecoureussite(self.prochainchemin,ben)
        pass
    
    """si la transaction est valide renvoie le benefice(potentiellement 0) sinon renvoie false"""
    def effectuertransaction(self,world,chemin):
        #verifier que la ville de depart est la bonne et autres preconditions
        if self.ville != chemin[0]:
            print("chemin invalide: mauvais depart")
            return False
        if world.nbvilles < self.ville:
            print("la ville du marchand est hors de l'index")
            return False
        if world.nbvilles < chemin[0]:
            print("la ville de départ est hors de l'index")
            return False
        if world.nbvilles < chemin[1]:
            print("la ville d'arriv�e est hors de l'index")
            return False
        if self.ville<0 or chemin[0]<0 or chemin[1]<0:
            print("index négatif pour une ville: c'est interdit")
            return False
        #verifier qu'il y a assez de produit a acheter
        cout=world.evaluercoutproduit(chemin[2],chemin[0])
        if cout<self.argent:#verification que l'on a l'argent necessaire
            if world.prendreproduit(chemin[2],chemin[0]):#achat
                self.argent=self.argent-cout#payement
                self.associerville(chemin[1])#voyage
                gain=world.evaluercoutproduit(chemin[2],chemin[1])#determiner le gain
                self.argent=self.argent+gain-1#gagner l'argent
                world.donnerproduit(chemin[2],chemin[1])#changer la quantit� de produit
                benefice = gain - cout#calcul du benefice
                return benefice
        else:
            print("trop pauvre")
            
        self.argent=self.argent-1
        print("impossible de faire la transaction")
        print(self.argent)
        return -1
    
    def associercomportement(self,comportement):
        self.comportement=comportement
        pass
    def associerville(self,ville):
        self.ville=ville
        pass