import math

class Cercle:
    def __init__(self, rayon) -> None:
        self.rayon = rayon
        
    def changerRayon(self, valeur):
        self.rayon = valeur
    
    def circonference(self):
        return 2 * math.pi * self.rayon
    def aire(self):
        return math.pi * (self.rayon ** 2)
    def diametre(self):
        return self.rayon * 2
    
    def afficherInfos(self):
        print("Circonference: ", self.circonference())
        print("Aire: ", self.aire())
        print("Diametre: ", self.diametre())

mon_cercle = Cercle(4)
mon_cercle.afficherInfos()
mon_cercle.changerRayon(10)
mon_cercle.afficherInfos()