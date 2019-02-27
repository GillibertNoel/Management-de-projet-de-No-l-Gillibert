
class Merchant(object):
    def __init__(self, villeinit = None, argentinit = 20, comportementinit = None) -> None:
        self.ville = villeinit
        self.argent = argentinit
        self.comportement = comportementinit
    def choisirtransaction(self):
        pass
    def passeruntour(self):
        pass
    def effectuertransaction(self,chemin):
        pass
    def associercomportement(self,comportement):
        pass
    def associerville(self,ville):
        pass