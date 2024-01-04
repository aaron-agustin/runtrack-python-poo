import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

    def lancerJeu(self):
        self.choisirNiveau()

        # Définir les points de vie en fonction du niveau
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 70
        elif self.niveau == 3:
            vie_joueur = 60
            vie_ennemi = 90
        else:
            print("Niveau invalide. Choisissez un niveau entre 1 et 3.")
            return

        # Instancier les personnages
        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        # Déroulement de la partie
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu!")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu. Game over!")
                break

        # Vérifier qui a gagné
        if joueur.vie > 0:
            print("Félicitations! Vous avez gagné!")
        elif ennemi.vie > 0:
            print("Dommage! Vous avez perdu!")

# Utilisation du jeu
jeu = Jeu()
jeu.lancerJeu()
