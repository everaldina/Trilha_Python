from dataclasses import dataclass
from resitic import Trilha, Residente
import pandas as pd
import os

@dataclass
class Residencia():
    __trilhas: list[Trilha]
    
    def __init__(self, trilhas: list[str] = None):
        if trilhas:
            self.trilhas = []
            for trilha in trilhas:
                self.add_trilha(trilha)
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
        if nome_trilha in self.get_trilhas():
            raise ValueError("Trilha já cadastrada")
        
        trilha = Trilha(nome_trilha)
        
        self.trilhas.append(trilha)
        
    def add_residente(self, nome_trilha: str, residenteDict: dict) -> None:
        trilha = self.get_trilha(nome_trilha)
        
        if not trilha:
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
    
    def get_trilhas(self) -> list[str]:
        return [trilha.nome for trilha in self.trilhas]
        
    def get_trilha(self, nome_trilha: str) -> Trilha:
        for trilha in self.trilhas:
            if trilha.nome == nome_trilha:
                return trilha
        return None
    
    def get_residentes(self) -> pd.DataFrame:
        dataframes_trilha = []
        
        for trilha in self.trilhas:
            residentes = trilha.get_identificadores()
            coluna_trilha = [trilha.nome]*len(residentes)
            index = pd.MultiIndex.from_arrays([coluna_trilha, residentes], names=['identificador', 'trilha'])
            residentes_trilha = trilha.residentes.set_index(index)
            dataframes_trilha.append(residentes_trilha)
        
        return pd.concat(dataframes_trilha).drop(columns=['identificador'])
    
    def save(self, path = None) -> None:
        data_frame = self.get_residentes()
        if path is None:
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))

            # Constroi o caminho para o diretório 'data' dentro do pacote1
            caminho_dados = os.path.join(diretorio_atual, 'data')

            # cria o diretório 'data' se ele não existir
            if not os.path.exists(caminho_dados):
                os.makedirs(caminho_dados)

            # caminho completo para o arquivo CSV
            caminho_csv = os.path.join(caminho_dados, 'residencia.csv')
            
            data_frame.to_csv(caminho_csv, index=True)
        else:
            caminho_csv = os.path.join(path)
            data_frame.to_csv(caminho_csv, index=True)