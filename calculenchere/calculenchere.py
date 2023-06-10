# fonction qui calcule l'enchère


def calcul_enchere(sellprice,profit,transport,fret,repair,exchangerate):
    EUR_CFA=657.01
    enchere= sellprice - transport*exchangerate - (profit+repair+fret)
    return enchere*exchangerate*EUR_CFA

def calcul_marge(sellprice, transport, fret, repair, exchangerate):
    EUR_CFA=657.01
    profit= sellprice - transport*exchangerate - (repair + fret)
    return profit*exchangerate*EUR_CFA