from DataFruta_V1 import AnaliseDados
from DataFruta_V1 import Data

class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
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
            lista_ordenada = sorted(self.__lista)
            tamanho = len(self.__lista)

            if len(self.__lista) % 2 == 0:
                mediana =  lista_ordenada[(tamanho // 2)-1]
            else:
                mediana =  lista_ordenada[tamanho // 2]
            
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
        strLista = "--------Lista ordenada de Datas--------\n"
        for data in self.__lista:
            strLista += str(data) + "\n"
        return strLista
    
    def listarEmOrdem(self):
        '''
            Este método mostra a lista de datas em ordem.
            Para isso ele usa o metodo sorted() que retorna
            uma lista ordenada.
            O metodo sorted() (assim como o sort()) utiliza 
            o metodo __lt__ (operador <) para comparar os 
            elementos da lista, então como ele ja esta 
            implementado na classe Data não é necessário
            implementar um algoritmo de ordenação.
        '''
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