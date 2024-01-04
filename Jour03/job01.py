class Ville:
    def __init__(self, nom, nombre_habitants):
        self.nom = nom
        self._nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self._nombre_habitants

    def augmenter_population(self):
        self._nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouterPopulation(self):
        self.ville.augmenter_population()


# Créer un objet Ville avec comme arguments “Paris” et 1000000.
paris = Ville("Paris", 1000000)

# Afficher en console le nombre d’habitants de la ville de Paris.
print(f"Nombre d'habitants de Paris : {paris.get_nombre_habitants()}")

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
marseille = Ville("Marseille", 861635)

# Afficher en console le nombre d’habitants de la ville de Marseille.
print(f"Nombre d'habitants de Marseille : {marseille.get_nombre_habitants()}")

# Créer les objets suivants :
# - John, 45 ans, habitant à Paris
# - Myrtille, 4 ans, habitant à Paris.
# - Chloé, 18 ans, habitant à Marseille.
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajouter la population après l'arrivée de ces nouvelles personnes.
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
print(f"Nombre d'habitants de Paris : {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants de Marseille : {marseille.get_nombre_habitants()}")
