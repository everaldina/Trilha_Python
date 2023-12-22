from DataFruta_V1 import AnaliseDados

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    @property
    def lista(self):
        return self.__lista.copy()
    
    def add(self, data):
        self.__lista.append(data)

    def mediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if len(self.__lista) == 0:
            return None
        else:
            listaOrdenada = sorted(self.__lista)

            tam = len(listaOrdenada)

            if tam <= 0:
                return None

            if tam % 2 == 0:
                mediana = listaOrdenada[(tam // 2) - 1]
            else:
                mediana = listaOrdenada[(tam // 2)]

            return mediana

    def menor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if len(self.__lista) == 0:
            return None
        else:
            return min(self.__lista)

    def maior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if len(self.__lista) == 0:
            return None
        else:
            return max(self.__lista)

    def __str__(self):
        strLista = "--------Lista de Nomes--------\n"

        for nome in self.__lista:
            strLista += nome + "\n"
        
        return strLista
    
    def listarEmOrdem(self):
        if len(self.__lista) == 0:
            return None
        else:
            listaOrdenada = sorted(self.__lista)

            return listaOrdenada
        
    def mediaAritmetica(self):
        return None

    def mediaGeometrica(self):    
        return None

    def mediaHarmonica(self):
        return None

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
        return None
    
    def varianciaPopulacional(self):
        return None
    
    def desvioPadraoAmostral(self):
        return None
    
    def varianciaAmostral(self):
        return None