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
        
        
    def add_trilha_dataframe(self, nome_trilha: str, trilha: pd.DataFrame) -> None:
        if nome_trilha in self.trilhas:
            raise ValueError("Trilha já cadastrada")
        
        if not isinstance(trilha, pd.DataFrame):
            raise TypeError("Trilha não é do tipo DataFrame")
        
        
        self.trilhas.append(nome_trilha)
        
        index = [(nome_trilha, trilha.loc[i, 'identificador']) for i in range(len(trilha))]
        
        index = pd.MultiIndex.from_tuples(index, names=['trilha', 'identificador'])
        
        if self.residencia.empty:
            self.residencia = trilha.set_index(index).drop(columns=['identificador'])
        else:
            self.residencia = pd.concat([self.residencia, trilha.set_index(index).drop(columns=['identificador'])])
            
    def get_trilha(self, nome_trilha: str) -> pd.DataFrame:
        if nome_trilha not in self.trilhas:
            return None
        
        return self.residencia.loc[nome_trilha]
    
    def get_residentes(self) -> pd.DataFrame:
        dataframes_trilha = []
        
        for trilha in self.trilhas:
            residentes = trilha.get_identificadores()
            coluna_trilha = trilha.nome*len(residentes)
            index = pd.MultiIndex.from_arrays([coluna_trilha, residentes], names=['identificador', 'trilha'])
            residentes_trilha = trilha.residentes.set_index(index)
            dataframes_trilha.append(residentes_trilha)
        
        return pd.concat(dataframes_trilha)
    
    def get_trilhas(data: pd.DataFrame) -> list[Trilha]:
        trilhas = []
        for trilha in data.index.get_level_values(0).unique():
            self.__trilhas.append(Trilha(trilha))
    
    def save(self, path = None) -> None:
        if path is not None:
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))

            # Constroi o caminho para o diretório 'data' dentro do pacote1
            caminho_dados = os.path.join(diretorio_atual, 'data')

            # cria o diretório 'data' se ele não existir
            if not os.path.exists(caminho_dados):
                os.makedirs(caminho_dados)

            # caminho completo para o arquivo CSV
            caminho_csv = os.path.join(caminho_dados, 'residencia.csv')
            
            self.residencia.to_csv(caminho_csv, index=True)
        else:
            caminho_csv = os.path.join(path, 'residencia.csv')
            self.residencia.to_csv(caminho_csv, index=True)
        
    def load(path = None) -> 'Residencia':
        if path is not None:
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))

            # Constroi o caminho para o diretório 'data' dentro do pacote1
            caminho_dados = os.path.join(diretorio_atual, 'data')

            # cria o diretório 'data' se ele não existir
            if not os.path.exists(caminho_dados):
                raise FileNotFoundError("Arquivo não encontrado")

            # caminho completo para o arquivo CSV
            caminho_csv = os.path.join(caminho_dados, 'residencia.csv')
            dados = pd.read_csv(caminho_csv, index_col=[0, 1])
            return Residencia(dados)
        else:
            caminho_csv = os.path.join(path, 'residencia.csv')
            dados = pd.read_csv(caminho_csv, index_col=[0, 1])
            return Residencia(dados)
        
