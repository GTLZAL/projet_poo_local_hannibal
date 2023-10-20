class Personnage: 

    def __init__(self,pPrénom,pNom,pAge):
        self.prenom = pPrénom
        self.nom = pNom
        self.__age= pAge

    def afficher_details(self) : 
         print(f"Nom : {self.nom}")
         print(f"Prénom : {self.prenom}")
         

class Local:
    def __init__(self, local_id):
        self.local_id = local_id
        self.occupant = None

    def louer_local(self,personne): 
        self.occupant = personne
    
    def afficher_details_occupant(self): 
        print(f"local : {self.local_id}")
        if self.occupant: 
            print ("occupant du local :")
            self.occupant.afficher_details()
        else : 
            print(" Ce local est actuellement vide")

# créa objet 
personne1 = Personnage("clement", "John", 30)
personne2 = Personnage("bob", "daoud", 25)


local1 = Local(101)
local2 = Local(102)

#location local 
local1.louer_local(personne1)
local2.louer_local(personne2)

#affichage détails 
local1.afficher_details_occupant()
local2.afficher_details_occupant()

local1.louer_local(personne2)
local1.afficher_details_occupant()
