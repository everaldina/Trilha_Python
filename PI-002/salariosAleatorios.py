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


"""
import random

class ListaSalario:
    def __init__(self, salarios):
        self.salarios = salarios

def geraListaSalario(n, sMin=1000, sMax=5000):
    salarios_gerados = []
    for _ in range(n):
        salario = random.uniform(sMin, sMax)
        salarios_gerados.append(salario)
    
    return ListaSalario(salarios_gerados)

lista_salarios = geraListaSalario(5)
print(lista_salarios.salarios)

"""
