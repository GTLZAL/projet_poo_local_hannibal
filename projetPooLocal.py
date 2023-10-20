class Personne:
    """
    Cette classe représente une personne avec des attributs tels que le nom, le prénom et l'âge.

    Attributes:
        nom (str): Le nom de la personne.
        prenom (str): Le prénom de la personne.
        __age (int): L'âge de la personne (notez le double underscore, ce qui le rend "privé").
    """

    def __init__(self, nom, prenom, age):
        """
        Initialise une nouvelle instance de la classe Personne.

        Args:
            nom (str): Le nom de la personne.
            prenom (str): Le prénom de la personne.
            age (int): L'âge de la personne.

        Note:
            L'âge est stocké en tant qu'attribut privé (avec un double underscore).
        """
        self.nom = nom
        self.prenom = prenom
        self.__age = age

    def afficher_details(self):
        """
        Affiche les détails de la personne, y compris le nom, le prénom et l'âge.

       
        """
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Âge : {self.__age}")


class Local:
    """
    Cette classe représente un local avec des attributs tels que son identifiant, sa capacité, son occupant (le cas échéant),
    et le prix par heure pour l'utilisation du local.

    Attributes:
        local_id (int): L'identifiant unique du local.
        occupant (Personne or None): La personne occupant actuellement le local, ou None s'il est vide.
        capacite (int): La capacité maximale du local.
        prix_par_heure (float): Le coût par heure d'utilisation du local.
    """

    def __init__(self, local_id, capacite, prix_par_heure):
        """
        Initialise une instance de la classe Local.

        Args:
            local_id (int): L'identifiant unique du local.
            capacite (int): La capacité maximale du local.
            prix_par_heure (float): Le coût par heure d'utilisation du local.
        """
        self.local_id = local_id
        self.occupant = None
        self.capacite = capacite
        self.prix_par_heure = prix_par_heure

    def allouer_local(self, personne):
        """
        Alloue le local à une personne si le local est actuellement vide.

        Args:
            personne (Personne): La personne à qui le local doit être alloué.

     
        """
        if not self.occupant:
            self.occupant = personne
            print(f"Le local {self.local_id} est désormais occupé par {personne.prenom}.")
        else:
            print(f"Le local {self.local_id} est déjà occupé par {self.occupant.prenom}.")

    def liberer_local(self):
        """
        Libère le local en le rendant disponible.

        
        """
        if self.occupant:
            self.occupant = None
            print(f"Le local {self.local_id} a été libéré.")
        else:
            print(f"Le local {self.local_id} est déjà vide.")

    def calculer_cout(self, heures):
        """
        Calcule le coût total d'utilisation du local pour un certain nombre d'heures.

        Args:
            heures (float): Le nombre d'heures pour lesquelles le local a été utilisé.

        Returns:
             Le coût total d'utilisation du local.
        """
        return self.prix_par_heure * heures


class Reservation:
    """
    Cette classe gère les réservations de locaux et leur disponibilité.

    Attributes:
        locaux_disponibles (dict): Un dictionnaire qui stocke les locaux disponibles, avec leur identifiant en clé
            et l'objet Local correspondant en valeur.
        reservations_clients (dict): Un dictionnaire qui stocke les réservations des clients, avec la personne en clé
            et une liste de tuples (local, heures) en valeur, représentant les locaux réservés et le nombre d'heures restantes.
    """

    def __init__(self):
        """
        Initialise une instance de la classe Reservation.
        """
        self.locaux_disponibles = {}
        self.reservations_clients = {}

    def ajouter_local(self, local):
        """
        Ajoute un local à la liste des locaux disponibles.

        Args:
            local (Local): L'objet Local à ajouter.

        Returns:
            None
        """
        self.locaux_disponibles[local.local_id] = local

    def louer_local(self, local_id, personne, heures):
        """
        Permet à une personne de louer un local pour un certain nombre d'heures, si le local est disponible.

        Args:
            local_id (int): L'identifiant du local à louer.
            personne (Personne): La personne qui effectue la réservation.
            heures (float): Le nombre d'heures à réserver.

        Returns:
            None
        """
        # Vérifier si le local est disponible
        if local_id in self.locaux_disponibles:
            local = self.locaux_disponibles[local_id]
            if local.capacite > 0 and heures > 0:
                local.capacite -= 1
                local.allouer_local(personne)
                if local.capacite == 0:
                    del self.locaux_disponibles[local_id]
                # Ajouter la réservation à la liste des réservations du client
                if personne in self.reservations_clients:
                    self.reservations_clients[personne].append((local, heures))
                else:
                    self.reservations_clients[personne] = [(local, heures)]
            else:
                print("Impossible de réserver. Le local est complet ou le nombre d'heures est invalide.")
        else:
            print(f"Le local {local_id} n'est pas disponible.")

    def liberer_local(self, local_id):
        """
        Libère un local réservé, le rendant disponible à nouveau.

        Args:
            local_id (int): L'identifiant du local à libérer.

        Returns:
            None
        """
        if local_id in self.locaux_disponibles:
            local = self.locaux_disponibles[local_id]
            if local.occupant:
                local.capacite += 1
                local.liberer_local()
                self.locaux_disponibles[local_id] = local
                # Supprimer la réservation correspondante
                for personne, reservations in self.reservations_clients.items():
                    for reservation in reservations:
                        if reservation[0].local_id == local_id:
                            reservations.remove(reservation)
                            break
            else:
                print(f"Le local {local_id} est vide.")
        else:
            print(f"Le local {local_id} n'est pas valide.")

    def calculer_cout_total(self, personne):
        """
        Calcule le coût total des réservations d'une personne.

        Args:
            personne (Personne): La personne pour laquelle calculer le coût.

        Returns:
            float: Le coût total des réservations de la personne.
        """
        cout_total = 0
        if personne in self.reservations_clients:
            for local, heures_restantes in self.reservations_clients[personne]:
                cout_local = local.calculer_cout(heures_restantes)
                cout_total += cout_local
        return cout_total
    
    def liberer_toutes_les_reservations(self, personne):
        """
        Libère toutes les réservations d'une personne.

        Args:
            personne (Personne): La personne dont les réservations doivent être libérées.

        Returns:
            None
        """
        if personne in self.reservations_clients:
            reservations = self.reservations_clients[personne]
            for local, heures_restantes in reservations:
                local.liberer_local()
            del self.reservations_clients[personne]

    def afficher_reservations(self, personne):
        """
        Affiche les réservations en cours d'une personne.

        Args:
            personne (Personne): La personne pour laquelle afficher les réservations.

        Returns:
            None
        """
        if personne in self.reservations_clients:
            print(f"Réservations pour {personne.prenom}:")
            for local, heures_restantes in self.reservations_clients[personne]:
                print(f"Local {local.local_id}, {heures_restantes} heures restantes.")
        else:
            print(f"Aucune réservation pour {personne.prenom}.")

# Exemple d'utilisation
personne1 = Personne("Doe", "John", 30)
personne2 = Personne("Smith", "Alice", 25)

local1 = Local("Salle A", 10, 5)
local2 = Local("Salle B", 6, 8)

reservation = Reservation()

# Ajoutons les locaux disponibles
reservation.ajouter_local(local1)
reservation.ajouter_local(local2)

# Louer les locaux
reservation.louer_local("Salle A", personne1, int(input("Entrez le nombre d'heures que vous voulez réserver pour la Salle A : ")))
reservation.louer_local("Salle B", personne2, int(input("Entrez le nombre d'heures que vous voulez réserver pour la Salle B : ")))

# Calculer le coût total des réservations pour personne1
cout_total_personne1 = reservation.calculer_cout_total(personne1)
print(f"Coût total des réservations pour {personne1.prenom}: {cout_total_personne1} euros")
# Calculer le coût total des réservations pour personne2
cout_total_personne2 = reservation.calculer_cout_total(personne2)
print(f"Coût total des réservations pour {personne2.prenom}: {cout_total_personne2} euros")

# Libérer toutes les réservations de personne2
reservation.liberer_toutes_les_reservations(personne2)

# Vérifier que les réservations de personne2 ont été libérées
reservation.afficher_reservations(personne2)  # Cela devrait afficher "Aucune réservation pour Alice"

reservation.afficher_reservations(personne1)