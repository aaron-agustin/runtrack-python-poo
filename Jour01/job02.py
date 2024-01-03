class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __repr__(self):
        return f'<Operation(nombre1={self.nombre1}, nombre2={self.nombre2})>'


# Création d'une instance de la classe Operation avec des valeurs spécifiques
operation_instance = Operation(nombre1=12, nombre2=3)

# Impression des valeurs des attributs nombre1 et nombre2 dans le format souhaité
print(f"Le nombre01 est {operation_instance.nombre1}")
print(f"Le nombre02 est {operation_instance.nombre2}")
