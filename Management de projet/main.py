# coding: utf-8
from monde import World
from merchant import Merchant
from merchantgridai import MerchantGridAI
import geretours
mondemain = World(nbvilles = 20, nbproduits = 20, grille = [])
paul = Merchant(villeinit=0)
paul.associercomportement(MerchantGridAI(mondemain))
pierre = Merchant(villeinit=1)
pierre.associercomportement(MerchantGridAI(mondemain))
marchandgroupe=[paul]
for i in range(0,100):
    for j in range(0,10):
        geretours.faireuntour(mondemain,marchandgroupe)
    marchandgroupe = geretours.faireuntourgenerantmarchand(mondemain,marchandgroupe)
for i in range(0,len(marchandgroupe)):
    print(marchandgroupe[i].argent)
print(len(marchandgroupe))