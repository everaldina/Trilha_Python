from dataclasses import dataclass
import numpy as np

class NotasTurma:
    '''
    Classe que representa as notas de uma turma em uma
    determinada disciplina.
    Utilizar atributos declarados como fracamente privados.
    '''
    def __init__(self, nAlunos = 30, nCreditos = 3):
        '''
        Construtor da classe NotasTurma.
        Entrada:
            nAlunos: número de alunos da turma
            nCreditos: número de créditos da disciplina
        '''
        self.__notas = np.zeros((nAlunos, nCreditos), dtype='float64')
        
    
    @property
    def notas(self):
        return self.__notas.copy()
    
    def getNotasAluno(self, index = 0):
        '''
        Retorna as notas do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            notas do aluno de índice index
        '''
        return self.__notas[index].copy()
    
    def getNotasAvaliacao(self, index = 0):
        '''
        Retorna as notas da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            notas da turma na avaliação de índice index
        '''
        return self.__notas[:, index].copy()

    def leNotas(self):
        '''
        Lê as notas dos alunos da turma.
        '''
        try:
            for i in range(len(self.__notas)):
                for j in range(len(self.__notas[i])):
                    self.__notas[i][j] = float(input(f"Digite a nota do aluno {i+1} na avaliação {j+1}: "))
            self.__notas = np.round(self.__notas, 2)
        except Exception:
            print("Nota inválida.")
            return

    def mediaTurma(self):
        '''
        Retorna a média da turma.
        Saída:
            média da turma
        '''
        return self.__notas.mean().mean()
    
    def mediaAritmeticaAluno(self, index = 0):
        '''
        Retorna a média aritmetica do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            média do aluno de índice index
        '''
        return self.__notas[index].mean()

    def mediaAritmeticaAvaliacao(self, index = 0):
        '''
        Retorna a média aritimetica da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            média da turma na avaliação de índice index
        '''
        return self.__notas[:, index].mean()
    
    def mediaGeometricaAluno(self, index = 0):
        '''
        Retorna a média geometrica do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            média do aluno de índice index
        '''
        return np.prod(self.__notas[index])**(1/len(self.__notas[index]))
    
    def mediaGeometricaAvaliacao(self, index = 0):
        '''
        Retorna a média geometrica da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            média da turma na avaliação de índice index
        '''
        return np.prod(self.__notas[:, index])**(1/len(self.__notas[:, index]))
    
    def mediaHarmonicaAluno(self, index = 0):
        '''
        Retorna a média harmonica do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            média do aluno de índice index
        '''
        return len(self.__notas[index]) / np.sum(1/self.__notas[index])
    
    def mediaHarmonicaAvaliacao(self, index = 0):
        '''
        Retorna a média harmonica da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            média da turma na avaliação de índice index
        '''
        return len(self.__notas[:, index]) / np.sum(1/self.__notas[:, index])

    def medianaAluno(self, index = 0):
        '''
        Retorna a mediana do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            mediana do aluno de índice index
        '''
        return np.median(self.__notas[index])
    
    def medianaAvaliacao(self, index = 0):
        '''
        Retorna a mediana da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            mediana da turma na avaliação de índice index
        '''
        return np.median(self.__notas[:, index])
    
    def medianaInferiorAluno(self, index = 0):
        '''
        Retorna a média inferior do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            média inferior do aluno de índice index
        '''
        return np.percentile(self.__notas[index], 25)
    
    def medianaInferiorAvaliacao(self, index = 0):
        '''
        Retorna a média inferior da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            média inferior da turma na avaliação de índice index
        '''
        return np.percentile(self.__notas[:, index], 25)
    
    def medianaSuperiorAluno(self, index = 0):
        '''
        Retorna a média superior do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            média superior do aluno de índice index
        '''
        return np.percentile(self.__notas[index], 75)
    
    def medianaSuperiorAvaliacao(self, index = 0):
        '''
        Retorna a média superior da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            média superior da turma na avaliação de índice index
        '''
        return np.percentile(self.__notas[:, index], 75)
    
    
    def quantAprovados(self):
        '''
        Retorna a quantidade de alunos aprovados (media >= 7).
        Saída:
            quantidade de alunos aprovados
        '''
        medias = self.__notas.mean(axis=1)
        
        return len(medias[medias >= 7])
    
        
    def quantReprovados(self):
        '''
        Retorna a quantidade de alunos reprovados (media < 7).
        Saída:
            quantidade de alunos reprovados
        '''
        medias = self.__notas.mean(axis=1)
        
        return len(medias[medias < 7])
    
    def menorNota(self):
        '''
        Retorna a menor nota da turma.
        Saída:
            menor nota da turma em cada avaliação e 
            na media final
        '''
        return self.__notas.min().min()

    def maiorNota(self):
        '''
        Retorna a maior nota da turma.
        Saída:
            maior nota da turma em cada avaliação e 
            na media final
        '''
        return self.__notas.max().max()
    
    def desvioPadraoPopulacionalAluno(self, index = 0):
        '''
        Retorna o desvio padrão populacional do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            desvio padrão populacional do aluno de índice index
        '''
        return np.std(self.__notas[index])
    
    def desvioPadraoPopulacionalAvaliacao(self, index = 0):
        '''
        Retorna o desvio padrão populacional da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            desvio padrão populacional da turma na avaliação de índice index
        '''
        return np.std(self.__notas[:, index])
    
    
    def varianciaPopulacionalAluno(self, index=0):
        '''
        Retorna a variância populacional do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            variância populacional do aluno de índice index
        '''
        return np.var(self.__notas[index])
    
    def varianciaPopulacionalAvaliacao(self, index=0):
        '''
        Retorna a variância populacional da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            variância populacional da turma na avaliação de índice index
        '''
        return np.var(self.__notas[:, index])
    
    def desvioPadraoAmostralAluno(self, index = 0):
        '''
        Retorna o desvio padrão amostral do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            desvio padrão amostral do aluno de índice index
        '''
        return np.std(self.__notas[index], ddof=1)
    
    def desvioPadraoAmostralAvaliacao(self, index = 0):
        '''
        Retorna o desvio padrão amostral da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            desvio padrão amostral da turma na avaliação de índice index
        '''
        return np.std(self.__notas[:, index], ddof=1)
    
    
    def varianciaAmostralAluno(self, index=0):
        '''
        Retorna a variância amostral do aluno de índice index.
        Entrada:
            index: índice do aluno
        Saída:
            variância amostral do aluno de índice index
        '''
        return np.var(self.__notas[index], ddof=1)
    
    def varianciaAmostralAvaliacao(self, index=0):
        '''
        Retorna a variância amostral da turma na avaliação de índice index.
        Entrada:
            index: índice da avaliação
        Saída:
            variância amostral da turma na avaliação de índice index
        '''
        return np.var(self.__notas[:, index], ddof=1)
    
    def __str__(self):
        i = 0
        strNotas = "--------Notas da Turma--------\n"
        for notas in self.__notas:
            strNotas += f"Aluno {i}: {notas[0]:.2f}\t{notas[1]:.2f}\t{notas[2]:.2f}\n"
            i += 1
        return strNotas
    
    def geraDados(self):
        '''
        Gera dados aleatórios para a turma.
        '''
        notas = np.random.uniform(0, 10, self.__notas.shape)
        self.__notas = np.round(notas, 2)