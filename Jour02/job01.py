class Rectangle:
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur
    
    def accesLongueur(self):
        return self.__longueur
    def accesLargeur(self):
        return self.__largeur
    
    def muterLongueur(self, valeur):
        self.__longueur = valeur
    def muterLargeur(self, valeur):
        self.__largeur = valeur
    
    
mon_rectangle = Rectangle(10,25)
mon_carre = Rectangle(15,15)
print(mon_rectangle.accesLongueur(),mon_rectangle.accesLargeur())
print(mon_carre.accesLongueur(),mon_carre.accesLargeur())
mon_rectangle.muterLargeur(45)
mon_carre.muterLongueur(12)
print(mon_rectangle.accesLongueur(),mon_rectangle.accesLargeur())
print(mon_carre.accesLongueur(),mon_carre.accesLargeur())