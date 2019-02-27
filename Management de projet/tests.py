from matplotlib.pyplot import bone

#tests des marchands
test1
    creermarchand
    verifier que decrementer argent d�cr�mente de 1 l'argent du marchand
    
test2
    creerunmonde
    incrementerproduit(monde,ville1,produit)
    creermarchand
    positionnermarchand ville1
    faireunvoyage(monde,ville1,ville2,produit)
    verifier que l'argent gagn� est le bon
    verifier que la quantit� de produit a bien �t� d�cr�ment� de 1 dans ville 1 et incr�ment� de 1 dans ville 2
    v�rifier que le marchand a chang� de position
    
test3
    creerunmonde
    creermarchand
    creercomportementmarchand
    associercomportementetmarchand
    verifier que l'association s'est bien pass�e.
    
test4
    creerunmonde
    creermarchand
    positionnermarchand ville1
    faireunvoyage(monde,ville1,ville2,produit)
    verifier que l'argent gagn� est le bon(0)
    verifier que le monde n'a pas chang�
    verifier que le marchand a chang� de position
    
test5
    creerunmonde
    creermarchand
    faireunvoyage(monde,ville1,ville2,produit)
    verifier que cela fait une erreur
    
test6
    creerunmonde
    creermarchand
    positionnermarchand ailleurs que dans ville1
    faireunvoyage(monde,ville1,ville2,produit)
    verifier que cela fait une erreur
    
test7
    creerunmonde
    creermarchand
    positionnermarchand dans ville1
    faireunvoyage(monde,ville1,ville1,produit)
    verifier que cela fait une erreur(dans ce monde fictif ce genre de boursicotage est interdit)
    #plus tard les mondes pourraient avoir une option pour autoriser cette tactique
    
test8:
    creerunmarchand
    verifier qu'il � la bonne quantit�e d'argent initial
    faireuntour
    verifier qu'il a un d'argent de moins
#test des mondes
test1
    creerunmonde
    verifier que le nombre de villes est le bon
    
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