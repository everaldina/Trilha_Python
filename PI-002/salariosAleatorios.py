import random

class ListaSalarios:
    def __init__(self, lista):
        self.lista = lista

    @classmethod
    def geraListaSalarios(cls, quantidade, salario_min=1000, salario_max=5000):
        salarios_gerados = [random.randint(salario_min, salario_max) for _ in range(quantidade)]
        return cls(salarios_gerados)


quantidade_de_salarios = 20
salarios = ListaSalarios.geraListaSalarios(quantidade_de_salarios)
print(salarios.lista)
