class Produit:
    def __init__(self, nom, prixHT, TVA) -> None:
        self.nom = nom 
        self.prixHT = prixHT
        self.TVA = TVA
        self.prixTTC = self.CalculerPrixTTC()
    
    def CalculerPrixTTC(self):
        return self.prixHT + self.prixHT * (self.TVA / 100)
    
    def afficher(self):
        return [self.nom,self.prixHT,self.TVA, self.prixTTC]
    
    #Getters
    def getNom(self):
        return self.nom
    def getPrixHT(self):
        return self.prixHT
    def getTVA(self):
        return self.TVA
    def getPrixTTC(self):
        return self.prixTTC
    
    #Setters
    def setNom(self, nom):
        self.nom = nom
    def setPrixHT(self, prixHT):
        self.prixHT = prixHT
        self.updatePrixTTC()
    def setTVA(self, taux):
        self.TVA = taux
        self.updatePrixTTC()
    def updatePrixTTC(self):
        self.prixTTC = self.CalculerPrixTTC()
        
baguette = Produit("Baguette", 0.5, 14)

print(baguette.getPrixTTC())
baguette.setNom("Banette")
baguette.setPrixHT(1)
print(baguette.getPrixTTC())