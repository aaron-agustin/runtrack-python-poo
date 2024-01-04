class Livre:
    def __init__(self, titre, auteur, nombrePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = nombrePages
    
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
mon_livre.getAuteur()
mon_livre.getTitre()
mon_livre.getNombrePages()
mon_livre.setNombrePages(155)
mon_livre.getNombrePages()
mon_livre.setNombrePages(3.5)