class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée horizontale (x) est : {self.x}")

    def afficherY(self):
        print(f"La coordonnée verticale (y) est : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

# Exemple d'utilisation de la classe Point
point1 = Point(2, 3)

# Affichage des coordonnées initiales
point1.afficherLesPoints()

# Affichage de la coordonnée horizontale (x)
point1.afficherX()

# Affichage de la coordonnée verticale (y)
point1.afficherY()

# Changement de la coordonnée horizontale (x)
point1.changerX(5)

# Changement de la coordonnée verticale (y)
point1.changerY(7)

# Affichage des nouvelles coordonnées
point1.afficherLesPoints()
