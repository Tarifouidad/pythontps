class Batiment:
    def __init__(self,adress):
        self.adress=adress
    def get_adress(self):
        return self.adress
    def set_adress(self,adress):
        self.adress=adress
    def __str__(self):
        return f"Ladress du batiment:{self.adress}"
class Maison(Batiment):
    def __init__(self,adress,nbPieces):
        super().__init__(adress)
        self.nbPieces=nbPieces
    def get_nbPieces(self):
        return self.nbPieces

    def set_nbPieces(self, nbPieces):
        self.nbPieces = nbPieces

    def __str__(self):
        return f"Maison, Adresse : {self.adress}, Nombre de pièces : {self.nbPieces}"
class Immeuble(Batiment):
    def __init__(self, adress, nbAppart):
        super().__init__(adress)
        self.nbAppart = nbAppart

    def get_nbAppart(self):
        return self.nbAppart

    def set_nbAppart(self, nbAppart):
        self.nbAppart = nbAppart

    def __str__(self):
        return f"Immeuble, Adresse : {self.adress}, Nombre d'appartements : {self.nbAppart}"

# Test des classes
batiment = Batiment("123 Rue de la Ville")
print(batiment)

maison = Maison("456 Avenue des Fleurs", 5)
print(maison)

immeuble = Immeuble("789 Boulevard Principal", 10)
print(immeuble)    