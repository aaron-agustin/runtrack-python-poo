class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe Personnage
personnage = Personnage()

# Affichage de la position initiale
print("Position initiale:", personnage.position())

# Déplacement vers la droite
personnage.droite()

# Affichage de la nouvelle position
print("Nouvelle position après déplacement à droite:", personnage.position())

# Déplacement vers le bas
personnage.bas()

# Affichage de la nouvelle position
print("Nouvelle position après déplacement vers le bas:", personnage.position())
