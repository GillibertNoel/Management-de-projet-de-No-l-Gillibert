# coding: utf-8
from monde import World
from merchant import Merchant
from merchantgridai import MerchantGridAI
import geretours
mondemain = World(nbvilles = 4, nbproduits = 2, grille = [])
paul = Merchant(villeinit=0)
paul.associercomportement(MerchantGridAI(mondemain))
pierre = Merchant(villeinit=1)
pierre.associercomportement(MerchantGridAI(mondemain))
marchandgroupe=[paul]
for i in range(0,100):
    geretours.faireuntour(mondemain,marchandgroupe)
print(paul.comportement.grille)
print(paul.argent)