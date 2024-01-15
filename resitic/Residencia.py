from dataclasses import dataclass
import pandas as pd
import os

@dataclass
class Residencia():
    __trilhas: list[str]
    __residencia: pd.DataFrame
    __colunas: list[str]
    
    def __init__(self, data: pd.DataFrame = None):
        self.__colunas = ['identificador']
        if data is not None:
            self.__trilhas = data.index.get_level_values('trilha').unique()
            self.__residencia = data
        else:
            self.__residencia = pd.DataFrame(columns=self.__colunas)
            self.__trilhas = []
        
    @property
    def trilhas(self) -> list[str]:
        return self.__trilhas
    
    @trilhas.setter
    def trilhas(self, trilhas: list[str]) -> None:
        self.__trilhas = trilhas
        
    @property
    def residencia(self) -> pd.DataFrame:
        return self.__residencia
    
    @residencia.setter
    def residencia(self, residencia: pd.DataFrame) -> None:
        self.__residencia = residencia
        
    def add_trilha(self, nome_trilha: str, trilha: pd.DataFrame) -> None:
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
    
    def save(self) -> None:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Constroi o caminho para o diretório 'data' dentro do pacote1
        caminho_dados = os.path.join(diretorio_atual, 'data')

        # cria o diretório 'data' se ele não existir
        if not os.path.exists(caminho_dados):
            os.makedirs(caminho_dados)

        # caminho completo para o arquivo CSV
        caminho_csv = os.path.join(caminho_dados, 'residencia.csv')
        
        self.residencia.to_csv(caminho_csv, index=True)
        
    def load() -> 'Residencia':
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
        
