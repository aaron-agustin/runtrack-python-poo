class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut : {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"Tâche '{tache.titre}' supprimée de la liste.")
        else:
            print("La tâche n'existe pas dans la liste.")

    def marquerCommeFinie(self, tache):
        if tache in self.taches:
            tache.statut = "terminée"
            print(f"Tâche '{tache.titre}' marquée comme terminée.")
        else:
            print("La tâche n'existe pas dans la liste.")

    def afficherListe(self):
        print("Liste des tâches :")
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list

# Tester le code
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 5", "à faire")
tache3 = Tache("Nettoyer la maison", "Aspirer et laver le sol")
tache4 = Tache("Envoyer le rapport", "Rapport mensuel pour le projet XYZ", "à faire")

liste_taches = ListeDeTaches()

# Ajouter des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)
liste_taches.ajouterTache(tache4)

# Afficher la liste des tâches
liste_taches.afficherListe()

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie(tache2)

# Afficher la liste des tâches après la modification
liste_taches.afficherListe()

# Filtrer les tâches à faire
taches_a_faire = liste_taches.filterListe("à faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)

# Supprimer une tâche de la liste
liste_taches.supprimerTache(tache3)

# Afficher la liste finale des tâches
liste_taches.afficherListe()
