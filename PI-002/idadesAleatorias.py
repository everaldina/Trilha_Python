import random

class ListaIdade:
    def __init__(self, lista):
        self.lista = lista

    @classmethod
    def geraListaIdades(cls, quantidade, idade_min=18, idade_max=65):
        idades_geradas = [random.randint(idade_min, idade_max) for _ in range(quantidade)]
        return cls(idades_geradas)


quantidade_de_idades = 20
idades = ListaIdade.geraListaIdades(quantidade_de_idades)
print(idades.lista)

"""
import random

class ListaIdade:
    def __init__(self, idades):
        self.idades = idades

def geraListaIdade(n, iMin=18, iMax=65):
    idades_geradas = []
    for _ in range(n):
        idade = random.randint(iMin, iMax)
        idades_geradas.append(idade)
    
    return ListaIdade(idades_geradas)

# Exemplo de uso:
lista_idades = geraListaIdade(20)  # Gera uma lista de 5 idades com valores padrão
print(lista_idades.idades)

"""