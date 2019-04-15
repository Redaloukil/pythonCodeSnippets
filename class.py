SEXE = (
    ("0" , "homme"),
    ("1" , "femme"),
    ("2" , "nakch"),
)

class Creature():
    name = ""
    
    def __str__(self):
        return self.name + self.winZedte 

    def __init__(self , name , winZedte):
        self.name = name
        self.winZedte = winZedte
        print("has been created")

class Homme(Creature):
    nom = ""
    prenom = ""
    age = None  
    
    def __str__(self):
        return self.name + self.winZedte 






reda = Person("Reda" , "Oran Castors") 
reda2 = Person("Mohamed" , "Oran Castors") 