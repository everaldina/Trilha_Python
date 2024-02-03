# Trilha_Python
Repositório para práticas da trilha de Python para o Programa de Residência em Tecnologia da Informação e da Comunicação (TIC18).

## Ambiente de desenvolvimento
Para desenvolvimento de codigos foi usando um ambiente virtual Anaconda na versão Python 3.11, as dependencias e mais detalhes desse ambiente estao disponiveis na pasta de [documentacao](documentacao/).

## [DataFruta](datafruta/)
Pacote com diferentes tipos de daados que implementam metodos estaticos basicos como media, mediana, maior e menor elemento.

## [DataFruta_V1](DataFruta_V1/)
Versão aprimorada do pacote datafruta, contando com novos tipos de medidas estatisticas, como:

- Médias e medidas de valor central:
    - Média aritmética dos dados
    - Média aritmética dos dados
    - Média geométrica dos dados
    - Média harmônica dos dados
    - Mediana (valor do meio) dos dados
    - Mediana inferior dos dados
    - Mediana superior dos dados
- Medidas de espalhamento
    - Desvio padrão populacional dos dados
    - Variância populacional dos dados
    - Desvio padrão amostral dos dados
    - Variância amostral dos dados
  
## [resitic](resitic/)
Pacote para coleta de dados sobre residentes de diferenças trilhas. O programa possui interface grafica e trabalha com dataframes do pandas. 

As dependencias do pacote estao disponiveis no arquivo [requirements.txt](resitic/requirements.txt). Para instalação dos requisitos, basta executar o comando `pip install -r requirements.txt` na pasta do pacote.

## [datasets](datasets/)
Pasta com datasets usados para as praticas.
1. Datasets de estações metereologicas de Salvador nos anos de 2003, 2013 e 2023 (Fonte: [Instituo Nacional de Meteorologia](https://portal.inmet.gov.br/dadoshistoricos)).
 - estacao_Salvador_2003.CSV
 - estacao_Salvador_2013.CSV
 - estacao_Salvador_2023.CSV

## [PI-002](PI-002.ipynb)
Notebook com a resolução do problema PI-002, que consiste em testes para comprar a eficiencia de metodos estaticos do datafruta com metodos de arrays do numpy.

Foi criado para os testes metodos em datafruta que geram dados aleatorios para salarios e idades.

## [PI-003](PI-003.ipynb)
Notebook com a resolução do problema PI-003, que consiste em testes para comprar a eficiencia de metodos estaticos de metodos implementados na classe DataFruta_V1 com metodos de arrays do numpy.

## [PI-004](PI-004.ipynb)
Notebook com a resolução do problema PI-004, que compara a eficiciecia de metodos estaticos nativos do numpy da classe [NotasTurma](DataFruta_V1/NotasTurma.py), com metodos estaticos implementado sem uso de ufunc.

## [PI-005](PI-005.ipynb)
Notebook com a resolução do problema PI-005, onde é criado series e dataframes com dados de residentes. Praticas de criação de series e dataframes, manipulação de dados, e visualização de dados são feitas nessa pratica.

## [PI-007](PI-007.ipynb)
Notebook com a resolução do problema PI-007, onde sao pegos dados de estações metereologicas de Salvador nos anos de 2003, 2013 e 2023 (disponivel em: [datasets](datasets/)). Os datasets saõ unificados e as medidas de temperatura e precipitacao sao analizadas.

Para o desenvolvimento dessa pratica, foram usados indices multiplos de ano, mes e dia, e tambem foram usados metodos de agrupamento de dados.

## Equipe
 - Everaldina Guimaraes Barbosa (egbarbosa.cic@uesc.br)
 - Ian Robert Luz Pinheiro (irlpinheiro.ege@uesc.br)
 - João Manoel Almeida Olivera (jmaoliveira.cic@uesc.br)
 - Nairan Bento Dos santos (nairanbsantos28@gmail.com)
  
## Membros anteriores
 - Vinicius Lima da Silva (vlsilva.ege@uesc.br)
 - Marcos Vinícius Tavares Gomes (mvtgomes.ege@uesc.br)
