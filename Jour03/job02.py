class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self._numero_compte}")
        print(f"Nom : {self._nom}")
        print(f"Prénom : {self._prenom}")
        print(f"Solde : {self._solde} €")
        print(f"Découvert autorisé : {self._decouvert}")

    def afficherSolde(self):
        print(f"Solde actuel : {self._solde} €")

    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self._solde} €")

    def retrait(self, montant):
        if self._decouvert or (self._solde - montant >= 0):
            self._solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self._solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux_agios):
        if self._solde < 0:
            agios = abs(self._solde) * taux_agios
            self._solde -= agios
            print(f"Agios appliqués. Nouveau solde : {self._solde} €")

    def virement(self, compte_destinataire, montant):
        if (self._decouvert or self._solde >= montant) and montant > 0:
            self._solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire._numero_compte}.")
        else:
            print("Virement impossible. Solde insuffisant.")

# Création d'un compte
compte1 = CompteBancaire(numero_compte="123456", nom="Dupont", prenom="Jean", solde=1000)

# Affichage des détails du compte
compte1.afficher()

# Versement sur le compte
compte1.versement(500)

# Retrait du compte
compte1.retrait(200)

# Affichage du solde
compte1.afficherSolde()

# Création d'un compte à découvert
compte2 = CompteBancaire(numero_compte="789012", nom="Martin", prenom="Sophie", solde=-200, decouvert=True)

# Virement du compte1 vers le compte2
compte1.virement(compte_destinataire=compte2, montant=300)

# Affichage des détails des deux comptes après le virement
compte1.afficher()
compte2.afficher()
