from dataclasses import dataclass

@dataclass
class Residente():
    __identificador: str
    __idade: int
    __formacao: int
    __formacaoGeral: int
    __formacaoEspecifica: str
    __andamentoGraduacao: float
    __tempoFormacao: int
    __experienciaPrevia: int
    
    def __init__(self, identificador: str = None):
        self.__identificador = identificador
    
    @property
    def identificador(self) -> str:
        return self.__identificador
        
    @identificador.setter
    def identificador(self, identificador: str) -> None:
        self.__identificador = identificador
    
    @property
    def idade(self) -> int:
        return self.__idade
    
    @idade.setter
    def idade(self, idade: int) -> None:
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
                
        self.__idade = idade
        
    @property
    def formacao(self) -> int:
        return self.__formacao
    
    @formacao.setter
    def formacao(self, formacao: int) -> None:
        if formacao not in [0, 1, 2, 3]:
            raise ValueError("Formação não cadastrada")
        
        self.__formacao = formacao
        
    @property
    def formacaoGeral(self) -> int:
        return self.__formacaoGeral
    
    @formacaoGeral.setter
    def formacaoGeral(self, formacaoGeral: int) -> None:
        if formacaoGeral and self.formacao == 0:
            raise ValueError("Formação geral não pode ser cadastrada para formação técnica")
        
        if self.formacao is None:
            raise ValueError("Formação não informada")
        
        if formacaoGeral not in [0, 1] and self.formacao != 0:
            raise ValueError("Formação geral não cadastrada")
        
        self.__formacaoGeral = formacaoGeral
        
    @property
    def formacaoEspecifica(self) -> str:
        return self.__formacaoEspecifica
    
    @formacaoEspecifica.setter
    def formacaoEspecifica(self, formacaoEspecifica: str) -> None:
        if self.formacaoGeral not in [0, 1] and self.formacao != 0:
            raise ValueError("Formação específica não pode ser cadastrada sem formação geral")
        
        self.__formacaoEspecifica = formacaoEspecifica
        
    @property
    def andamentoGraduacao(self) -> float:
        return self.__andamentoGraduacao
    
    @andamentoGraduacao.setter
    def andamentoGraduacao(self, andamentoGraduacao: float) -> None:
        if self.formacao not in [1, 2] and andamentoGraduacao:
            raise ValueError("Andamento de graduação não pode ser cadastrado sem estar cursando graduação")
        
        self.__andamentoGraduacao = andamentoGraduacao
        
    @property
    def tempoFormacao(self) -> int:
        return self.__tempoFormacao
    
    @tempoFormacao.setter
    def tempoFormacao(self, tempoFormacao: int) -> None:
        if self.formacao != 3 and tempoFormacao:
            raise ValueError("Tempo de formação não pode ser cadastrado sem graduação concluída")
        
        self.__tempoFormacao = tempoFormacao
        
    @property
    def experienciaPrevia(self) -> int:
        return self.__experienciaPrevia
    
    @experienciaPrevia.setter
    def experienciaPrevia(self, experienciaPrevia: int) -> None:
        self.__experienciaPrevia = experienciaPrevia
        
    def __dict__(self):
        return {
            'identificador': self.identificador,
            'idade': self.idade,
            'formacao': self.formacao,
            'formacaoGeral': self.formacaoGeral,
            'formacaoEspecifica': self.formacaoEspecifica,
            'andamentoGraduacao': self.andamentoGraduacao,
            'tempoFormacao': self.tempoFormacao,
            'experienciaPrevia': self.experienciaPrevia
        }