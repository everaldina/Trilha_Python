from DataFruta_V1 import AnaliseDados
import random
import numpy as np

class ListaSalarios(AnaliseDados):
    __salario_minimo = 1320

    def __init__(self, lista = None):
        super().__init__(type(float))

        if lista is None:
            self.__lista = np.array([], dtype='float64')
        else:
            if not isinstance(lista, np.ndarray):
                raise TypeError("O tipo de dado deve ser np.ndarray")
            
            if lista.dtype != 'float64':
                raise TypeError("O tipo de dado deve ser np.ndarray com dtype='float64'")
            
            self.__lista = lista.copy()

    @property
    def lista(self):
        return self.__lista.copy()
    
    @property
    def salario_minimo(self):
        return self.__salario_minimo
    
    def add(self, data):
        if not isinstance(data, float):
            raise TypeError("O tipo de dado deve ser float")
        
        self.__lista = np.append(self.__lista, data)
    
    @classmethod
    def geraListaSalarios(cls, n, sMin=1320, sMax=10000):
        salarios_gerados = [random.uniform(sMin, sMax) for _ in range(n)]

        return cls(np.array(salarios_gerados, dtype='float64'))      

    def mediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if len(self.__lista) == 0:
            return None
        
        ordenados = self.lista
        ordenados.sort()
        tamanho = len(self.__lista)
        mediana = -1
        
        if tamanho % 2 == 0:
            mediana1 = ordenados[(tamanho // 2) - 1]
            mediana2 = ordenados[tamanho // 2]
            mediana = (mediana1 + mediana2) / 2
        else:
            mediana = ordenados[tamanho // 2]

        return mediana

    def menor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if len(self.__lista) == 0:
            return None
        else:
            menor = self.__lista[0]

            for i in self.__lista:
                if i < menor:
                    menor = i

            return menor

    def maior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if len(self.__lista) == 0:
            return None
        else:
            maior = self.__lista[0]

            for i in self.__lista:
                if i > maior:
                    maior = i

            return maior
    
    def __str__(self):
        strLista = "--------Lista de Salarios--------\n"
        for salario in self.__lista:
            strLista += str(salario) + "\n"
        return strLista
    
    def listarEmOrdem(self):
        if len(self.__lista) == 0:
            return None
        else:
            listaOrdenada = sorted(self.__lista)

            return listaOrdenada
        
    def mediaAritmetica(self):
        if len(self.__lista) == 0:
            return None
        else:
            soma = sum(self.__lista)
            
            media = soma / len(self.__lista)

            return media

    def mediaGeometrica(self):    
        if len(self.__lista) == 0:
            return None
        else:
            produto = 1

            for i in self.__lista:
                produto *= i
            
            media = produto ** (1 / len(self.__lista))

            return media

    def mediaHarmonica(self):
        if len(self.__lista) == 0:
            return None
        else:
            soma = 0

            for i in self.__lista:
                soma += 1 / i
            
            media = len(self.__lista) / soma

            return media

    def medianaInferior(self):
        if len(self.__lista) == 0:
            return None
        else:
            listaOrdenada = sorted(self.__lista)
            tamanho = len(self.__lista)

            mediana_inf = listaOrdenada[tamanho // 4] if tamanho % 2 == 0 else listaOrdenada[tamanho // 4]
            
            return mediana_inf

    def medianaSuperior(self):
        if len(self.__lista) == 0:
            return None
        else:
            listaOrdenada = sorted(self.__lista)
            tamanho = len(self.__lista)

            mediana_sup = listaOrdenada[(3 * tamanho) // 4] if tamanho % 2 == 0 else listaOrdenada[(3 * tamanho) // 4]
            
            return mediana_sup
    
    '''
    Medidas de Espalhamento
    '''

    def desvioPadraoPopulacional(self):
        if len(self.__lista) == 0:
            return None
        else:
            media = self.mediaAritmetica()
            somatorio = 0

            for i in self.__lista:
                somatorio += (i - media) ** 2
            
            desvio = (somatorio / len(self.__lista)) ** (1/2)

            return desvio
    
    def varianciaPopulacional(self):
        if len(self.__lista) == 0:
            return None
        else:
            media = self.mediaAritmetica()
            somatorio = 0

            for i in self.__lista:
                somatorio += (i - media) ** 2
            
            variancia = somatorio / len(self.__lista)

            return variancia
    
    def desvioPadraoAmostral(self):
        if len(self.__lista) == 0:
            return None
        else:
            media = self.mediaAritmetica()
            somatorio = 0

            for i in self.__lista:
                somatorio += (i - media) ** 2
            
            desvio = (somatorio / (len(self.__lista) - 1)) ** (1/2)
            
            return desvio
    
    def varianciaAmostral(self):
        if len(self.__lista) == 0:
            return None
        else:
            media = self.mediaAritmetica()
            somatorio = 0

            for i in self.__lista:
                somatorio += (i - media) ** 2
            
            variancia = somatorio / (len(self.__lista) - 1)

            return variancia