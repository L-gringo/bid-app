#classe qui définit un objet modèle 

class model:
    def __init__(self,name,year,sellprice=0,profit=0,fret=0,repfees=0):
        self.name=name
        self.year=year
        self.sellprice=sellprice
        self.profit=profit
        self.fret=fret
        self.repfees=repfees
    
    def display(self):
        print(f"c'est le modele {self.name} de l'année: {self.year}")
    
    def otherfees(self,sellprice,profit,fret):
        self.sellprice=sellprice
        self.profit=profit
        self.fret=fret
    
    def repmount(self,repair):
        self.repfees=repair
        print(f"les frais de réparation pour le modèle {self.name} {self.year} s'élèvent à: {self.repfees}")
        return self.repfees