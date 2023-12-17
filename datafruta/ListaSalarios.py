from datafruta import AnaliseDados

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    @property
    def lista(self):
        return self.__lista
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        print("------------------Entrada de Salarios------------------")
        # Pergunta a quantidade de elementos e verifica se é um número inteiro
        try:
            qnt = int(input("Quantidade de elementos na lista de salarios: "))
        except Exception:
            print("Quantidade inválida de elementos")
            return
        
        for i in range(qnt):
            salario = 0
            invalido = True
            while invalido:
                try:
                    salario = float(input("Digite o valor do salario: "))
                except:
                    print("Valor inválido.")
                
                if salario < 0:
                    print("Salario não pode ser nagativo")
                else:
                    self.__lista.append(salario)
                    print("Salario adicionado com sucesso!!")
                    invalido = False        

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de salarios vazia.")
            return
        ordenados = sorted(self.__lista)
        tamanho = len(self.__lista)
        mediana = -1
        if tamanho % 2 == 0:
            mediana1 = ordenados[(tamanho // 2) - 1]
            mediana2 = ordenados[tamanho // 2]
            mediana = (mediana1 + mediana2) / 2
        else:
            mediana = ordenados[tamanho // 2]

        print("Mediana de salarios: ", mediana)

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de salarios vazia.")
            return
        ordenada = sorted(self.__lista)
        menor = ordenada[0]
        print("Menor salario: ", menor)

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de salarios vazia.")
            return
        ordenada = sorted(self.__lista)
        maior = ordenada[-1]
        print("Maior salario: ", maior)
    
    def __str__(self):
        strLista = "--------Lista de Salarios--------\n"
        for salario in self.__lista:
            strLista += str(salario) + "\n"
        return strLista
    
    def listarEmOrdem(self):
        if len(self.__lista) == 0:
            print("Lista de salarios vazia.")
        else:
            listaOrdenada = sorted(self.__lista)

            print("--------Lista ordenada de Salarios--------")
            for salario in listaOrdenada:
                print(salario)

    def add(self, salario):
        self.__lista.append(salario)