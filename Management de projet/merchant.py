
class Merchant(object):
    def __init__(self, villeinit = None, argentinit = 20, comportementinit = None) -> None:
        self.ville = villeinit
        self.argent = argentinit
        self.comportement = comportementinit
    def choisirtransaction(self):
        self.prochainchemin = self.comportement.choisirchemin(self.ville)
        pass
    def passeruntour(self):
        self.effectuertransaction(self.prochainchemin)
        pass
    def effectuertransaction(self,chemin):
        #verifier que la ville de depart est la bonne et autres preconditions
        #verifier qu'il y a assez de produit a acheter
        #faire la transaction.
        pass
    def associercomportement(self,comportement):
        self.comportement=comportement
        pass
    def associerville(self,ville):
        self.ville=ville
        pass