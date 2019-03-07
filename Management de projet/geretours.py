# coding: utf-8
#pour organiser les tours
import random
def faireuntour(world,marchands):
    world.passeruntour()
    for i in marchands:
        i.choisirtransaction()
    random.shuffle(marchands)
    for i in marchands:
        i.passeruntour(world)