import pandas as pd

def main():
    #Exercicio 1
    identificador = ["tic18Py08200"]
    idade = [23]
    formação = [2]
    formaçãoGeral = [1]
    formaçãoEspecífica = ["Ciência da Computação"]
    andamentoGraduação = [0.6]
    tempoFormação = [None]
    experiênciaPrevia = [True]
    
    
    # Exercicio 2
    index = pd.Index(identificador, name="Identificador")
    print(index, end="\n\n")
    
    idade = pd.Series(idade)
    formação = pd.Series(formação)
    formaçãoGeral= pd.Series(formaçãoGeral)
    formaçãoEspecífica = pd.Series(formaçãoEspecífica)
    andamentoGraduação = pd.Series(andamentoGraduação)
    tempoFormação = pd.Series(tempoFormação)
    experiênciaPrevia = pd.Series(experiênciaPrevia)
    
    print("Média de idade: ", mediaIdade(idade))
    
    print("Formação predominante: ", formacaoPredominante(formação))
    
    print("Formação geral predominante: ", formacaoGeralPredominante(formaçãoGeral))
    
    
    # Exercicio 3
    
    
    
    
    
    
def mediaIdade(idades):
    return idades.mean()

def formacaoPredominante(formacoes):
    formacoesPosssiveis = {
        0: "Formação técnica.",
        1: "Formação técnica graduação em andamento",
        2: "Graduação em andamento",
        3: "Graduação concluída"
    }
        
    return formacoesPosssiveis[formacoes.mode()[0]]

def formacaoGeralPredominante(formacoesGerais):
    formacoesGeraisPosssiveis = {
        0: "Engenharia",
        1: "Computação"
    }
    
    return formacoesGeraisPosssiveis[formacoesGerais.mode()[0]]

if __name__ == '__main__':
    main()