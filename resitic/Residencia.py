from dataclasses import dataclass
from resitic import Trilha, Residente
import pandas as pd
import os

@dataclass
class Residencia():
    __trilhas: list[Trilha]
    __colunas: list[str]
    
    def __init__(self, trilhas: list[Trilha] = None, data: pd.DataFrame = None):
        if trilhas and data:
            raise ValueError("Não é possível passar trilhas e data ao mesmo tempo")
        if trilhas:
            self.__trilhas = trilhas
        elif data:
            self.__trilhas = []
            for trilha in data.index.get_level_values(0).unique():
                self.__trilhas.append(Trilha(trilha))
        else:
            self.__trilhas = []
        
    @property
    def trilhas(self) -> list[Trilha]:
        return self.__trilhas
    
    @trilhas.setter
    def trilhas(self, trilhas: list[Trilha]) -> None:
        self.__trilhas = trilhas
        
    @property
    def residencia(self) -> pd.DataFrame:
        return self.__residencia
    
    @residencia.setter
    def residencia(self, residencia: pd.DataFrame) -> None:
        self.__residencia = residencia
        
    def add_trilha(self, nome_trilha: str) -> None:
        for trilha in self.trilhas:
            if trilha.nome == nome_trilha:
                raise ValueError("Trilha já cadastrada")
        
        trilha = Trilha(nome_trilha)
        
        self.trilhas.append(trilha)
        
    def add_residente(self, nome_trilha: str, residenteDict: dict) -> None:
        trilha = None
        
        for trilha in self.trilhas:
            if trilha.nome == nome_trilha:
                break
        else:
            raise ValueError("Trilha não cadastrada")
        
        if nome_trilha == "python":
            id = "tic18Py"
        elif nome_trilha == "dotnet":
            id = "tic18Net"
        elif nome_trilha == "java":
            id = "tic18Jav"
        
        residente = Residente(id + residenteDict['identificador'])
        
        residente.idade = residenteDict['idade']
        residente.formacao = residenteDict['formacao']
        residente.formacaoGeral = residenteDict['formacaoGeral']
        residente.formacaoEspecifica = residenteDict['formacaoEspecifica']
        residente.andamentoGraduacao = residenteDict['andamentoGraduacao']
        residente.tempoFormacao = residenteDict['tempoFormacao']
        residente.experienciaPrevia = residenteDict['experienciaPrevia']
        
        trilha.addResidente(residente)