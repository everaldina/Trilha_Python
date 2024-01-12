import pandas as pd

def main():
    #Exercicio 1
    identificador = ["tic18Py08200", "tic18Py86001", "tic18Py05999"]
    idade = [23, 22, 24]
    formação = [1, 1, 2]
    formaçãoGeral = [1, 1, 0]
    formaçãoEspecífica = ["Ciência da Computação", "Ciência da Computação", "Engenharia Elétrica"]
    andamentoGraduação = [0.66, 0.66, 0.99]
    tempoFormação = [None, None, None]
    experiênciaPrevia = [True, True, True]
    
    
    # Exercicio 2
    index = pd.Index(identificador)
    idade = pd.Series(idade, index = index)
    formação = pd.Series(formação, index = index)
    formaçãoGeral= pd.Series(formaçãoGeral, index = index)
    formaçãoEspecífica = pd.Series(formaçãoEspecífica, index = index)
    andamentoGraduação = pd.Series(andamentoGraduação, index = index)
    tempoFormação = pd.Series(tempoFormação, index = index).fillna(0)
    experiênciaPrevia = pd.Series(experiênciaPrevia, index = index)
       
    
    print("Média de idade: ", mediaIdade(idade))
    
    print("Formação predominante: ", formacaoPredominante(formação))
    
    print("Formação geral predominante: ", formacaoGeralPredominante(formaçãoGeral))
    
    print()
    
    # Exercicio 3
    data = pd.DataFrame({'Idade': idade, 'Formação': formação, 
                         'Formação Geral': formaçãoGeral, 'Formação Específica': formaçãoEspecífica, 
                         'Andamento Graduação': andamentoGraduação, 'Tempo Formação': tempoFormação, 
                         'Experiência Prévia': experiênciaPrevia}, index = index)
    
    print("Dataframe: ")
    print(data)
    
    
    
    
    
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