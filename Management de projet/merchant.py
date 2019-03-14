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
        self.argent=self.argent-1
        if self.ville != chemin[0]:
            raise CheminInvalide("chemin invalide: mauvais depart dans merchant.effectuertransaction")
            return False
        if world.nbvilles < self.ville:
            raise VilleHorsLimites("la ville du marchand est hors de l'index du monde dans lequel l'on apelle merchant.effectuertransaction")
            return False
        if world.nbvilles < chemin[0]:
            raise VilleHorsLimites("la ville de départ est hors de l'index du monde dans lequel l'on apelle merchant.effectuertransaction")
            return False
        if world.nbvilles < chemin[1]:
            raise VilleHorsLimites("la ville d'arrivée est hors de l'index du monde dans lequel l'on apelle merchant.effectuertransaction")
            return False
        if self.ville<0 or chemin[0]<0 or chemin[1]<0:
            raise VilleHorsLimites("index négatif pour une ville: c'est interdit erreur repérée dans merchant.effectuertransaction")
            return False
        if chemin[0]==chemin[1]:
            print("il est interdit de faire un chemin d'une ville a elle même")
        #verifier qu'il y a assez de produit a acheter
        cout=world.evaluercoutproduit(chemin[2],chemin[0])
        self.associerville(chemin[1])#voyage
        if cout<self.argent:#verification que l'on a l'argent necessaire
            if world.prendreproduit(chemin[2],chemin[0]):#achat
                self.argent=self.argent-cout#payement
                gain=world.evaluercoutproduit(chemin[2],chemin[1])#determiner le gain
                self.argent=self.argent + gain#gagner l'argent
                world.donnerproduit(chemin[2],chemin[1])#changer la quantit� de produit
                benefice = gain - cout - 1#calcul du benefice
                return benefice
        print("impossible de faire la transaction: trop pauvre ou n'a pas de produit a acheter")
        print(self.argent)
        return -1
    
    def associercomportement(self,comportement):
        self.comportement=comportement
        pass
    def associerville(self,ville):
        self.ville=ville
        pass