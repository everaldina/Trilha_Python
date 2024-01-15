from dataclasses import dataclass
from resitic import Residente
import pandas as pd

@dataclass
class Trilha():
    __residentes: pd.DataFrame
    __nome: str
    
    def __init__(self, nome: str = None):
        self.__residentes = pd.DataFrame(columns=['identificador', 'idade', 'formacao', 'formacaoGeral', 'formacaoEspecifica', 'andamentoGraduacao', 'tempoFormacao', 'experienciaPrevia'])
        self.__nome = nome
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome
    
    @property
    def residentes(self) -> list[Residente]:
        return self.__residentes
    
    def addResidente(self, residente: Residente) -> None:
        self.residentes = self.residentes.append(residente)