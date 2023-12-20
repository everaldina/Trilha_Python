from datafruta import AnaliseDados
from datafruta import Data

class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []
    
    @property
    def lista(self):
        return self.__lista.copy()

    def add(self, data):
        self.__lista.append(data)   
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        
        
        print("------------------Entrada de datas------------------")
        # Pergunta a quantidade de elementos e verifica se é um número inteiro
        try:
            qnt = int(input("Quantidade de elementos na lista de datas: "))
        except Exception:
            print("Quantidade inválida de elementos")
            return
        
        for i in range(qnt):
            # Pergunta a data e verifica se é uma data válida
            invalido = True
            while(invalido):
                data = input("Digite a data no formato dd/mm/aaaa: ")
                try:
                    dia, mes, ano = data.split("/")
                    
                    if dia.isnumeric() == False:
                        raise ValueError("Dia inválido.")
                    if mes.isnumeric() == False:
                        raise ValueError("Mes inválido.")
                    if mes.isnumeric() == False:
                        raise ValueError("Ano inválido.")
                    
                    data = Data(int(dia), int(mes), int(ano))
                    self.__lista.append(data)
                    print("Data adicionada com sucesso!!")
                    invalido = False
                except ValueError as e:
                    print(str(e))
    
    def mostraMediana(self):
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
     
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
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