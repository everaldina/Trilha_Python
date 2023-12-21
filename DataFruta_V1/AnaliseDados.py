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
