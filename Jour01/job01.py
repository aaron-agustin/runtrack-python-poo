class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __repr__(self):
        return f'<Operation(nombre1={self.nombre1}, nombre2={self.nombre2})>'


operation_instance = Operation()


print(operation_instance)
