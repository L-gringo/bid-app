#classe pour créer un objet manufacturer

class manufacturer:
    def __init__(self,name,model={}):
        self.name=name
        self.model=model
    
    def display(self):
        print(f"Liste des modèles du Constructeur {self.name} : {self.model}")
