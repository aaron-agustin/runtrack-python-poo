class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nouveau_nom):
        self.prenom = nouveau_nom

    def afficher_infos(self):
        print(f"L'âge de l'animal {self.prenom} est {self.age} ans")

# Instanciation d'un objet Animal
mon_animal = Animal()

# Affichage de l'âge initial de l'animal
mon_animal.afficher_infos()

# Faire vieillir l'animal en appelant la méthode vieillir
mon_animal.vieillir()

# Affichage de l'âge de l'animal après avoir vieilli
mon_animal.afficher_infos()

# Nommer l'animal en appelant la méthode nommer
mon_animal.nommer("Luna")

# Affichage du nom de l'animal et de son âge
mon_animal.afficher_infos()
