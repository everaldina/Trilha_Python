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
