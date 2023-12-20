from datafruta import AnaliseDados
import random

class ListaIdades(AnaliseDados):
    
    def __init__(self, lista = []):
        super().__init__(type(int))
        self.__lista = lista.copy()      
    
    @property
    def lista(self):
        return self.__lista.copy()
    
    def add(self, data):
        self.__lista.append(data)   
        
    @classmethod
    def geraListaIdades(cls, n, iMin=18, iMax=65):
        idades_geradas = [random.randint(iMin, iMax) for _ in range(n)]
        return cls(idades_geradas)

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''

        print("--------------Entrada de idades--------------")
        try:
            qtde = int(input("Quantidade de idades a serem incluidas: "))
        except Exception:
            print("Quantidade inválida de idades.")
            return
        
        if qtde < 0:
            print("Quantidade inválida de idades.")
            return
        
        listaAuxiliar = []
        for i in range(qtde):
            try:
                idade = int(input("Idade: "))
            except Exception:
                print("Idade invalida.")
                return
            
            if idade < 0:
                print("Idade invalida.")
                return
            
            listaAuxiliar.append(idade)
        
        for i in listaAuxiliar:
            self.__lista.append(i)

    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''

        if len(self.__lista) == 0:
            return None
        
        listaAuxiliar = self.__lista.copy()
        listaAuxiliar.sort()
        tamanho = len(listaAuxiliar)
        mediana = 0

        if tamanho % 2 == 0:
            mediana = (listaAuxiliar[tamanho//2] + listaAuxiliar[(tamanho//2) - 1]) / 2
        else:
            mediana = listaAuxiliar[tamanho//2]

        return mediana  
    
    def mostraMenor(self):
        '''
        Este método retorna o menor elemento da lista
        '''

        if len(self.__lista) == 0:
            return None
        else:
            return min(self.__lista)
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''

        if len(self.__lista) == 0:
            return None
        else:
            return max(self.__lista)

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