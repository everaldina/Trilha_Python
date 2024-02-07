from DataFruta_V1 import AnaliseDados
import random
import numpy as np

class ListaIdades(AnaliseDados):
    
    def __init__(self, lista = None):
        super().__init__(type(int))

        if lista == None:
            self.__lista = np.array([], dtype='intc')
        else:
            if isinstance(lista, np.ndarray) and lista.dtype == 'intc':
                self.__lista = lista.copy()
            else:
                raise TypeError("O tipo de dado deve ser np.ndarray com dtype='intc'")
    
    @property
    def lista(self):
        return self.__lista.copy()
    
    def add(self, data):
        if not isinstance(data, int):
            raise TypeError("O tipo de dado deve ser int")
        
        self.__lista = np.append(self.__lista, data)
        
    @classmethod
    def geraListaIdades(n, iMin=18, iMax=65):
        idades_geradas = [random.randint(iMin, iMax) for _ in range(n)]
        return ListaIdades(np.array(idades_geradas, dtype='intc'))
    
    def mediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''

        if len(self.__lista) == 0:
            return None
        
        listaAuxiliar = self.lista
        listaAuxiliar.sort()
        tamanho = len(listaAuxiliar)
        mediana = 0

        if tamanho % 2 == 0:
            mediana = (listaAuxiliar[tamanho//2] + listaAuxiliar[(tamanho//2) - 1]) / 2
        else:
            mediana = listaAuxiliar[tamanho//2]

        return mediana  
    
    def menor(self):
        '''
        Este método retorna o menor elemento da lista
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
        strLista = "--------Lista de Idades--------\n"

        for i in self.__lista:
            strLista += i + "\n"
        
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