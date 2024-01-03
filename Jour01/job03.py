class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __repr__(self):
        return f'<Operation(nombre1={self.nombre1}, nombre2={self.nombre2})>'

    def addition(self):
        result = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est :", result)
        return result

# Création d'une instance de la classe Operation avec des valeurs spécifiques
operation_instance = Operation(nombre1=12, nombre2=3)

# Appel de la méthode addition et affichage du résultat en console
operation_instance.addition()
