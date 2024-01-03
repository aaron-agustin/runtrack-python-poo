class Personne:
    def __init__(self, nom="", prenom=""):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

# Instanciation de plusieurs personnes avec des valeurs initiales
personne1 = Personne(nom="Doe", prenom="John")
personne2 = Personne(nom="Dupond", prenom="Jean")

# Appel de la méthode SePresenter pour vérifier que tout fonctionne correctement
resultat1 = personne1.SePresenter()
resultat2 = personne2.SePresenter()

# Affichage des résultats en console
print(resultat1)
print(resultat2)
