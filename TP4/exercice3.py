from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    @abstractmethod
    def gains(self):
        pass

class Patron(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.salaire = salaire

    def get_salaire(self):
        return self.salaire

    def set_salaire(self, salaire):
        self.salaire = salaire

    def __str__(self):
        return f"Patron: {super().__str__()}, Salaire: {self.salaire}"

    def gains(self):
        return self.salaire

class TravailleurCommission(Employe):
    def __init__(self, nom, prenom, salaire, commission, quantite):
        super().__init__(nom, prenom)
        self.salaire = salaire
        self.commission = commission
        self.quantite = quantite

    def get_salaire(self):
        return self.salaire

    def set_salaire(self, salaire):
        self.salaire = salaire

    def get_commission(self):
        return self.commission

    def set_commission(self, commission):
        self.commission = commission

    def get_quantite(self):
        return self.quantite

    def set_quantite(self, quantite):
        self.quantite = quantite

    def __str__(self):
        return f"Travailleur à commission: {super().__str__()}, Salaire de base: {self.salaire}, Commission: {self.commission}, Quantité: {self.quantite}"

    def gains(self):
        return self.salaire + self.commission * self.quantite

class TravailleurHoraire(Employe):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self.retribution = retribution
        self.heures = heures

    def get_retribution(self):
        return self.retribution

    def set_retribution(self, retribution):
        self.retribution = retribution

    def get_heures(self):
        return self.heures

    def set_heures(self, heures):
        self.heures = heures

    def __str__(self):
        return f"Travailleur horaire: {super().__str__()}, Rémunération horaire: {self.retribution}, Heures de travail: {self.heures}"

    def gains(self):
        return self.retribution * self.heures

# Test des classes avec polymorphisme
employes = [
    Patron("Smith", "John", 5000),
    TravailleurCommission("Doe", "Jane", 2000, 10, 100),
    TravailleurHoraire("Johnson", "Bob", 20, 160),
]

for employe in employes:
    print(employe)
    print(f"Gains: {employe.gains()}")
    print()  # Ligne vide pour séparer les informations des employés
