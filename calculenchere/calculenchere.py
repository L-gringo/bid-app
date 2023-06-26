# fonction qui calcule l'enchère


def calcul_enchere(sellprice,profit,transport,fret,repair,storage,taxes,salary,exchangerate):
   
    enchere= sellprice/exchangerate - (transport+fret+storage) - (profit+repair+taxes+salary)/exchangerate
    return enchere

def calcul_marge(sellprice, transport, fret, repair, taxes, storage, salary,exchangerate):
    
    profit= sellprice - (transport+storage)*exchangerate - repair - fret*exchangerate - taxes - salary
    return profit