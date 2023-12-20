from datafruta import AnaliseDados

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
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
        solicita a digitação de cada um deles.
        '''
        print("------------------Entrada de nomes------------------")
        try:
            qtde = int(input("Quantidade de nomes a serem incluidos: "))

            if qtde < 0:
                raise ValueError("Quantidade inválida de nomes.")
        except Exception:
            print("Quantidade inválida de nomes.")
            return

        for i in range(qtde):
            try:
                nome = input(f"Digite o nome {i+1}: ")
                self.__lista.append(nome)
            except Exception:
                print("Nome inválido.")
                i -= 1

    def mostraMediana(self):
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