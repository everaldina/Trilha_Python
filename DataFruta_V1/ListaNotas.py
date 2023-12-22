from datafruta import AnaliseDados

class ListaNotas(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
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
        print("------------------Entrada de Notas------------------")
        # Pergunta a quantidade de elementos e verifica se é um número inteiro
        try:
            qnt = int(input("Quantidade de elementos na lista de notas: "))
        except Exception:
            print("Quantidade inválida de elementos")
            return
        
        for i in range(qnt):
            nota = 0
            invalido = True
            while invalido:
                try:
                    nota = float(input("Digite a nota do aluno: "))
                except:
                    print("Valor inválido.")
                
                if nota < 0:
                    print("Uma nota nao pode ser negativa")
                else:
                    self.__lista.append(nota)
                    print("Nota adicionado com sucesso!!")
                    invalido = False        

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if len(self.__lista) == 0:
            return None
        ordenados = sorted(self.__lista)
        tamanho = len(self.__lista)
        mediana = -1
        if tamanho % 2 == 0:
            mediana1 = ordenados[(tamanho // 2) - 1]
            mediana2 = ordenados[tamanho // 2]
            mediana = (mediana1 + mediana2) / 2
        else:
            mediana = ordenados[tamanho // 2]

        return mediana

    def mostraMenor(self):
        '''
        Este método retorna o menor elemento da lista
        '''
        if len(self.__lista) == 0:
            return None
        
        menor = self.__lista[0]

        for i in self.__lista:
            if i < menor:
                menor = i
        
        return menor

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if len(self.__lista) == 0:
            return None
        
        maior = self.__lista[0]

        for i in self.__lista:
            if i > maior:
                maior = i
        
        return maior
    
    def __str__(self):
        strLista = "--------Lista de Notas--------\n"
        for nota in self.__lista:
            strLista += str(nota) + "\n"
        return strLista
    
    def listarEmOrdem(self):
        if len(self.__lista) == 0:
            return None
        else:
            listaOrdenada = sorted(self.__lista)

            return listaOrdenada
    

    '''
    Médias e Medidas de Valor Central
    ''' 

    def mediaAritmetica(self):
        if len(self.__lista) == 0:
            return None

        soma = 0
        for elemento in self.__lista:
            soma += elemento

        media_aritmetica = soma / len(self.__lista)

        return media_aritmetica

    def mediaGeometrica(self):    
        if len(self.__lista) == 0:
            return None

        produto = 1
        for elemento in self.__lista:
            produto *= elemento

        media_geom = produto ** (1 / len(self.__lista))

        return media_geom

    def mediaHarmonica(self):
        if len(self.__lista) == 0:
            return None

        soma_reciprocos = 0
        for elemento in self.__lista:
            soma_reciprocos += 1 / elemento

        media_harm = len(self.__lista) / soma_reciprocos

        return media_harm

    def medianaInferior(self):
        if len(self.__lista) == 0:
            return None

        ordenados = sorted(self.__lista)
        tamanho = len(self.__lista)
        mediana_inf = ordenados[tamanho // 4] if tamanho % 2 == 0 else ordenados[tamanho // 4]

        return mediana_inf

    def medianaSuperior(self):
        if len(self.__lista) == 0:
            return None

        ordenados = sorted(self.__lista)
        tamanho = len(self.__lista)
        mediana_sup = ordenados[(3 * tamanho) // 4] if tamanho % 2 == 0 else ordenados[(3 * tamanho) // 4]

        return mediana_sup
    
    '''
    Medidas de Espalhamento
    '''

    def desvioPadraoPopulacional(self):
        if len(self.__lista) < 2:
            return None

        media = self.mediaAritmetica()

        somatorio = 0
        for elemento in self.__lista:
            diferenca = elemento - media
            somatorio += diferenca * diferenca

        variancia = somatorio / len(self.__lista)
        desvio_padrao_pop = (variancia)**0.5

        return desvio_padrao_pop
    
    def varianciaPopulacional(self):
        if len(self.__lista) < 2:
            return None

        media = self.mediaAritmetica()

        somatorio = 0
        for elemento in self.__lista:
            diferenca = elemento - media
            somatorio += diferenca * diferenca

        variancia_pop = somatorio / len(self.__lista)

        return variancia_pop
    
    def desvioPadraoAmostral(self):
        if len(self.__lista) < 2:
            return None

        media = self.mediaAritmetica()

        somatorio = 0
        for elemento in self.__lista:
            diferenca = elemento - media
            somatorio += diferenca * diferenca

        variancia_amostral = somatorio / (len(self.__lista) - 1)
        desvio_padrao_amostral = variancia_amostral**0.5

        return desvio_padrao_amostral
    
    def varianciaAmostral(self):
        if len(self.__lista) < 2:
            return None

        media = self.mediaAritmetica()

        somatorio = 0
        for elemento in self.__lista:
            diferenca = elemento - media
            somatorio += diferenca * diferenca

        variancia_amostral = somatorio / (len(self.__lista) - 1)

        return variancia_amostral

    '''
    Métodos próprios para a classe ListaNotas
    '''
    def alunosComNotaMaiorQue(self, valor):
        return [nota for nota in self.__lista if nota > valor]

    def alunosComNotaMenorQue(self, valor):
        return [nota for nota in self.__lista if nota < valor]
    
    def aproximaNotasSete(self):
        for i in range(len(self.__lista)):
            if 6.9 < self.__lista[i] < 7:
                self.__lista[i] = 7
    
    def calcularModa(self):
        if len(self.__lista) == 0:
            return None
        contagem_notas = {nota: self.__lista.count(nota) for nota in set(self.__lista)}
        moda = max(contagem_notas, key=contagem_notas.get)
        return moda
    
    def alunosParaFinal(self):
        return [nota for nota in self.__lista if 1.66 < nota < 7]
    
    def alunosSemNotaParaFinal(self):
        return [nota for nota in self.__lista if nota < 1.67]
    
    def alunosAprovados(self):
        return [nota for nota in self.__lista if nota >= 7]
