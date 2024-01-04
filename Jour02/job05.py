class Voiture:
    def __init__(self, brand, model, year, mileage) -> None:
        self.__marque = brand
        self.__modele = model
        self.__annee = year
        self.__kilometrage = mileage
        self.__en_marche = False
        self.__reservoir = 50
    
    # Getters
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_kilometrage(self):
        return self.__kilometrage
    
    
    
    # Setters
    def set_marque(self,marque):
        self.__marque = marque
    def set_modele(self, modele):
        self.__modele = modele
    def set_annee(self, annee):
        self.__annee = annee
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    def set_en_marche(self, val):
        self.__en_marche = val
    def set_reservoir(self, val):
        self.__reservoir = val
        
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.set_en_marche(True)
    def arreter(self):
        self.set_en_marche(False)
        
    def __verifier_plein(self):
        return self.__reservoir
    
mowombi = Voiture()
mazomba = Voiture()

mowombi.demarrer()
mazomba.demarrer()