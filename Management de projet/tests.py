# coding: utf-8
from matplotlib.pyplot import bone

#tests des marchands
def merchanttest1():
    mondetest = World(nbvilles = 2, nbproduits = 1, grille = [])
    reussite=True
    mondetest.donnerproduit(0,0)
    marchandtest = Merchant()
    ordepart=marchandtest.argent
    marchandtest.associerville(0)
    marchandtest.faireunvoyage(mondetest,0,1,0)
    chaine="MTest1: "
    if (ordepart-marchandtest.argent==8):
        chaine=chaine+"la quantité d'argent gagnée est la bonne\n"
    else:
        chaine=chaine+"la quantité d'argent gagnée est la mauvaise\n"
        reussite=False
    if mondetest.grid[0][0]==0:#il faut 0 Produit 0 dans la ville 0
        chaine=chaine+"il y a bien 0 produit 0 dans la ville 0\n"
    else:
        chaine=chaine+"il y a la mauvaise quantité de produit 0 dans la ville 0\n"
        reussite=False
    if mondetest.grid[1][0]==1:#il faut 1 Produit 0 dans la ville 1
        chaine=chaine+"il y a bien 1 produit 0 dans la ville 1\n"
    else:
        chaine=chaine+"il y a la mauvaise quantité de produit 0 dans la ville 1\n"
        reussite=False
    if marchandtest.ville==1:#le marchand doit être allé dans la bonne ville
        chaine=chaine+"le marchand a voyagé dans la bonne ville\n"
    else:
        chaine=chaine+"le marchand n'a pas voyagé dans la bonne ville\n"
        reussite=False
    return chaine,reussite
    
def merchanttest2():
    mondetest = World(nbvilles = 1, nbproduits = 1, grille = [])
    marchandtest = Merchant()
    merchantgridai=MerchantGridAI(mondetest)
    marchandtest.associercomportement(merchantgridai)
    if marchandtest.comportement == merchantgridai:
        return True
    else:
        return False
    
def merchanttest3():
    mondetest = World(nbvilles = 2, nbproduits = 1, grille = [])
    reussite=True
    marchandtest = Merchant()
    ordepart=marchandtest.argent
    marchandtest.associerville(0)
    marchandtest.faireunvoyage(mondetest,0,1,0)
    chaine="MTest1: "
    if (ordepart-marchandtest.argent==-1):
        chaine=chaine+"la quantité d'argent gagnée est la bonne\n"
    else:
        chaine=chaine+"la quantité d'argent gagnée est la mauvaise\n"
        reussite=False
    if mondetest.grid[0][0]==0:#il faut 0 Produit 0 dans la ville 0
        chaine=chaine+"il y a bien 0 produit 0 dans la ville 0\n"
    else:
        chaine=chaine+"il y a la mauvaise quantité de produit 0 dans la ville 0\n"
        reussite=False
    if mondetest.grid[1][0]==0:#il faut 1 Produit 0 dans la ville 1
        chaine=chaine+"il y a bien 0 produit 0 dans la ville 1\n"
    else:
        chaine=chaine+"il y a la mauvaise quantité de produit 0 dans la ville 1\n"
        reussite=False
    if marchandtest.ville==1:#le marchand doit être allé dans la bonne ville
        chaine=chaine+"le marchand a voyagé dans la bonne ville\n"
    else:
        chaine=chaine+"le marchand n'a pas voyagé dans la bonne ville\n"
        reussite=False
    return chaine,reussite
    
def merchanttest4():
    mondetest = World(nbvilles = 2, nbproduits = 1, grille = [])
    marchandtest = Merchant()
    try:
        marchandtest.faireunvoyage(mondetest,0,1,0)
    except CheminInvalide:
        return True
    return False

def merchanttest5():
    mondetest = World(nbvilles = 2, nbproduits = 1, grille = [])
    marchandtest = Merchant()
    marchandtest.associerville(1)
    try:
        marchandtest.faireunvoyage(mondetest,0,1,0)
    except CheminInvalide:
        return True
    return False
def merchanttest6():
    mondetest = World(nbvilles = 2, nbproduits = 1, grille = [])
    marchandtest = Merchant()
    marchandtest.associerville(1)
    try:
        marchandtest.faireunvoyage(mondetest,0,0,0)
    except CheminInvalide:
        return True
    return False
    #plus tard les mondes pourraient avoir une option pour autoriser cette tactique

#test des mondes
def worldtest1():
    mondetest = World(nbvilles = 4, nbproduits = 3, grille = [])
    villes=0
    for i in mondetest.grille:
        villes=villes+1
    if mondetest.nbvilles==villes and villes==4 :
        return True
    else:
        return False
    
test2
    creerunmonde
    verifier que le nombre de produits est le bon

test3
    creerunmonde
    verifier que les productions sont des flotants
    
test4
    creerunmonde
    verifier que le nombre de produits produit par ville est bon
    
test5
    creerunmonde
    faireuntour
    verifier que les productions ont �t� appliqu�es
    faireuntour
    verifier que les productions ont �t� appliqu�es(au cas ou incrementer 0 n'est pas pareil qu'incrementer une autre valeur)
    
test6
    creerunmonde
    comparer ce monde avec lui m�me.(doit �tre vrai)
    
test7
    creerunmondeprecis
    creerunmondeidentique
    comparer ces deux mondes(doit �tre vrai)
    
test8
    creerunmonde
    creerunautremonde
    comparer ces deux mondes(doit �tre faux)
    
test9
    creerunmonde
    incrementerproduit ville
    verifier quantit� produit
    decrementerproduit m�me ville
    verifier quantit� produit et retour(doit �tre true)
    
test10
    creerunmonde
    decrementerproduit ville
    verifier que cela renvoie false
    verifier quantit� produit(doit �tre la m�me qu'avant)

#test du comportement des marchands
test1
    creerunmonde
    creerunmarchand
    creeruncomportementmarchand(marchand,monde)
    demander au comportement de choisir un chemin
    verifier que c'est bien un chemin (monde,ville1,ville2,produit)
    
test2
    creerunmonde
    creeruncomportementmarchand(monde)
    demander au comportement de choisir un chemin n fois
    verifier que cela suit bien la distribution pr�vue
    
test3
    creerunmonde
    creeruncomportementmarchand(monde)
    indiquer au comportement la reussite d'un chemin
    demander au comportement de choisir un chemin n fois
    verifier que cela suit bien la distribution pr�vue

test4
    creerunmonde
    creeruncomportementmarchand(monde)
    indiquer au comportement l'echec d'un chemin
    demander au comportement de choisir un chemin n fois
    verifier que cela suit bien la distribution pr�vue

test5
    creerunmonde
    creeruncomportementmarchand(monde)
    verifier que l'on n'a pas chang� le reste du monde.

"""Tests aux limites: verifier si l'on � des exceptions quand l'on applique des fonctions 
avec des valeurs de ville ou de produit negatifs ou superieurs au nombre de villes ou de produits
(suivant que c'est une valeur de ville ou de produit)"""