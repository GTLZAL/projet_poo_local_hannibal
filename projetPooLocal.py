class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.__age = age  # L'âge est privé

    def afficher_details(self):
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Âge : {self.__age}")


class Local:
    def __init__(self, local_id, capacite, prix_par_heure):
        self.local_id = local_id
        self.occupant = None
        self.capacite = capacite
        self.prix_par_heure = prix_par_heure

    def allouer_local(self, personne):
        if not self.occupant:
            self.occupant = personne
            print(f"Le local {self.local_id} est désormais occupé par {personne.prenom}.")
        else:
            print(f"Le local {self.local_id} est déjà occupé par {self.occupant.prenom}.")

    def liberer_local(self):
        if self.occupant:
            self.occupant = None
            print(f"Le local {self.local_id} a été libéré.")
        else:
            print(f"Le local {self.local_id} est déjà vide.")
         
    def calculer_cout(self, heures):
        """
        Calcule le coût total en fonction du nombre d'heures passées dans le local.

        :param heures: Le nombre d'heures pour lesquelles le local a été occupé.
        :return: Le coût total en fonction du prix par heure.
        """
        return self.prix_par_heure * heures


class Reservation:
    def __init__(self):
        self.locaux_disponibles = {}

    def louer_local(self, local, personne):
        if local in self.locaux_disponibles:
            if local.capacite > 0:
                local.capacite -= 1
                local.allouer_local(personne)
                if local.capacite == 0:
                    del self.locaux_disponibles[local]
            else:
                print(f"Impossible d'attribuer le local {local.local_id}, il est complet.")
        else:
            print(f"Le local {local.local_id} est déjà occupé.")

    def liberer_local(self, local):
        if local.occupant:
            local.capacite += 1
            local.liberer_local()
            self.locaux_disponibles[local] = True
        else:
            print(f"Le local {local.local_id} est vide.")
    

    
# Exemple d'utilisation
personne1 = Personne("Doe", "John", 30)
personne2 = Personne("Smith", "Alice", 25)

local1 = Local("Salle A", 10, 5)  # Tarif horaire de 5 euros et capacité 
local2 = Local("Salle B", 6, 8)   # Tarif horaire de 8 euros et capacité


reservation = Reservation()

# Louer la salle1 
reservation.louer_local(local1, personne1)
heures = int(input("Entrer le nombre d'heure que vous voulez : "))
cout_total = local1.calculer_cout(heures)
print(f"Le coût total pour la location de la salle {local1.local_id} pendant {heures} heures est de {cout_total} euros.")

# Libérer la salle1
reservation.liberer_local(local1)

# Louer la salle2 pour 3 heures
reservation.louer_local(local2, personne2)
heures = 3
cout_total = local2.calculer_cout(heures)
print(f"Le coût total pour la location de la salle {local2.local_id} pendant {heures} heures est de {cout_total} euros.")



