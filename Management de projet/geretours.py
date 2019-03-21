# coding: utf-8
#pour organiser les tours
from monde import World
from merchant import Merchant
from merchantgridai import MerchantGridAI
import random
def faireuntour(world,marchands):
    world.passeruntour()
    for i in marchands:
        i.choisirtransaction()
    random.shuffle(marchands)
    for i in marchands:
        i.passeruntour(world)
        
def faireuntourgenerantmarchand(world,marchands):
    marchands.append(Merchant(villeinit=0,comportementinit = MerchantGridAI(world)))
    world.passeruntour()
    for i in marchands:
        i.choisirtransaction()
    random.shuffle(marchands)
    for i in marchands:
        i.passeruntour(world)
        if i.argent<=1:
            marchands.remove(i)
    return marchands