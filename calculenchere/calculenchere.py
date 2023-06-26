# fonction qui calcule l'enchère


def calcul_enchere(sellprice,profit,transport,fret,repair,storage,taxes,salary,exchangerate):
   
    enchere= sellprice/exchangerate - (transport+fret+storage) - (profit+repair+taxes+salary)/exchangerate
    return enchere

def calcul_marge(sellprice, transport, fret, repair, taxes, storage, salary,exchangerate):
    
    profit= sellprice - (transport+storage)*exchangerate - repair - fret*exchangerate - taxes - salary
    return profit

enchere=calcul_enchere(5000000,350000,750,100,10000,49,48000,50000,601.38)
print (enchere)