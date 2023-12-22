from abc import ABC, abstractmethod

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def mediana(self):
        pass
    
    @abstractmethod
    def menor(self):
        pass

    @abstractmethod
    def maior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass

    
    #Média e medidas de valor central
    
    @abstractmethod
    def mediaAritmetica(self):
        pass
    
    @abstractmethod
    def mediaGeometrica(self):
        pass
    
    @abstractmethod
    def mediaHarmonica(self):
        pass
    
    @abstractmethod
    def medianaInferior(self):
        pass
    
    @abstractmethod
    def medianaSuperior(self):
        pass


    #Medidas de espalhamento

    @abstractmethod
    def desvioPadraoPopulacional(self):
        pass
    
    @abstractmethod
    def varianciaPopulacional(self):
        pass
    
    @abstractmethod
    def desvioPadraoAmostral(self):
        pass
    
    @abstractmethod
    def varianciaAmostral(self):
        pass

    
    # Métodos próprios para a classe ListaNotas
    
    @abstractmethod
    def alunosComNotaMaiorQue(self, valor):
        pass

    @abstractmethod
    def alunosComNotaMenorQue(self, valor):
        pass
    
    @abstractmethod
    def aproximaNotasSete(self):
        pass
    
    @abstractmethod
    def calcularModa(self):
        pass
    
    @abstractmethod
    def alunosParaFinal(self):
        pass
    
    @abstractmethod
    def alunosSemNotaParaFinal(self):
        pass
    
    @abstractmethod
    def alunosAprovados(self):
        pass
