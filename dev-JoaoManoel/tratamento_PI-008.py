import pandas as pd
import numpy as np

estacao_ssa_2003 = pd.read_csv('./datasets/estacao_Salvador_2003.CSV', header=8, sep=';', encoding='latin-1')
estacao_ssa_2013 = pd.read_csv('./datasets/estacao_Salvador_2013.CSV', header=8, sep=',', encoding='utf-8')
estacao_ssa_2023 = pd.read_csv('./datasets/estacao_Salvador_2023.CSV', header=8, sep=';', encoding='latin-1')

estacoes = [estacao_ssa_2003, estacao_ssa_2013, estacao_ssa_2023]

colunas_data = [
    'DATA (YYYY-MM-DD)',
    'HORA (UTC)',
    'Data',
    'Hora UTC'
]

colunas_gerais = [
    'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)',
    'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)',
    'TEMPERATURA DO PONTO DE ORVALHO (°C)',
    'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)',
    'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)',
    'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)',
    'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)',
]

for estacao in estacoes:
    for collumn in estacao.columns:        
        if collumn in colunas_gerais:
            estacao[collumn] = estacao[collumn].str.replace(',', '.')
            estacao[collumn] = estacao[collumn].astype(float)
        elif collumn in colunas_data:
            pass
        else:
            estacao.drop(collumn, axis=1, inplace=True)
    
    estacao.replace(['-9999', -9999, -9999.0, '-9999.0'], value= np.nan, inplace=True)
    
estacao_ssa_2003.to_pickle('./datasets/tratados/estacao_Salvador_2003.pkl')
estacao_ssa_2013.to_pickle('./datasets/tratados/estacao_Salvador_2013.pkl')
estacao_ssa_2023.to_pickle('./datasets/tratados/estacao_Salvador_2023.pkl')