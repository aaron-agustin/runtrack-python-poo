class Livre:
    def __init__(self, titre, auteur, nombrePages, disponible = True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = nombrePages
        self.__disponible = disponible
    
    def verification(self):
        if self.__disponible:
            return True
        else:
            return False

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"Vous avez emprunté le livre {self.__titre}")
        else:
            print("Le livre est indisponible")
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"Le livre {self.__titre} est à nouveau disponible")
        else:
            print("Le livre à deja été rendu")
            
    def getTitre(self):
        print(f"Le titre du livre est: {self.__titre}")
        return self.__titre
    def getAuteur(self):
        print(f"L'auteur de ce livre est: {self.__auteur}")
        return self.__auteur
    def getNombrePages(self):
        print(f"Nombre de pages: {self.__nombrePages}")
        return self.__nombrePages
    
    def setTitre(self, titre):
        self.__titre = titre
    def setAuteur(self, auteur):
        self.__auteur = auteur
    def setNombrePages(self, nb):
        if type(nb) == int and nb > 0:
            self.__nombrePages = nb
        else:
            print("Nombre de pages invalide. Veuillez rentrer un entier positif.")
        
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 93)
mon_livre.emprunter()
mon_livre.emprunter()
mon_livre.rendre()