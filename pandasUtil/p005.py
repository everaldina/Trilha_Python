import pandas as pd

def main():
    identificador = []
    idade = []
    formação = []
    formaçãoGeral = []
    formaçãoEspecífica = []
    andamentoGraduação = []
    tempoFormação = []
    experiênciaPrevia = []
    
    index = pd.Index(identificador)
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
    
def mediaIdade(idades):
    return idades.mean()

def formacaoPredominante(formacoes):
    formacoesPosssiveis = {
        0: "Formação técnica.",
        1: "Formação técnica graduação em andamento",
        2: "Graduação em andamento",
        3: "Graduação concluída"
    }
    
    return formacoesPosssiveis[formacoes.mode()]

def formacaoGeralPredominante(formacoesGerais):
    formacoesGeraisPosssiveis = {
        0: "Engenharia",
        1: "Computação"
    }
    
    return formacoesGeraisPosssiveis[formacoesGerais.mode]()

if __name__ == '__main__':
    main()