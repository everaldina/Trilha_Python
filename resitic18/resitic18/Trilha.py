from dataclasses import dataclass
from resitic18.Residente import Residente
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
    def residentes(self) -> pd.DataFrame:
        return self.__residentes
    
    @residentes.setter
    def residentes(self, residentes: list[Residente]) -> None:
        self.__residentes = residentes
    
    def addResidente(self, residente: Residente) -> None:
        if not isinstance(residente, Residente):
            raise TypeError("Residente não é do tipo Residente")
        
        if residente.identificador in list(self.residentes['identificador']):
            raise ValueError("Residente já cadastrado")
        
        index = len(self.residentes)
        
        self.residentes.loc[index] = residente.__dict__()
        
    def get_identificadores(self):
        return self.residentes['identificador'].values.tolist()
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Trilha):
            return False
        
        return self.nome == __value.nome