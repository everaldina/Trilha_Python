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
    
    '''
    Medidas de Espalhamento
    '''

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