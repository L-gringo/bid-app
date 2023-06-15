#class qui définit un objet utilisateur
from model.model import model
from streamlitdemo.database import db_items_list

class user:
    def __init__(self, username):
        
        self.username=username
        #self.password=password
    
    def displayMan(self,list_man,manufacturer):
        for man in list_man:
            if man.name==manufacturer:
                man.display()
    
    def setfees(self,sellprice,profit,fret,modele={}):
        for key in modele.keys():  
            modele1=model(key,modele[key])
            modele1.otherfees(sellprice,profit,fret)
            return modele1
    
    def transportfees(self,town):
      #  dict_StateTranspFees={"New York": 500, "Houston":800,"Washington":750}
        dict_StateTranspFees=db_items_list("Transports")
        for key in dict_StateTranspFees.keys():
            if key==town:
                print(f"les frais de transport s'élèvent à : {dict_StateTranspFees[key]}")
                return dict_StateTranspFees[key]
    
    def currencies(self,dev1,dev2):
        curr1=dev1
        curr2=dev2
        print (f"le taux de change sélectionné est la paire {curr1}/{curr2}") 
        return [dev1,dev2]
