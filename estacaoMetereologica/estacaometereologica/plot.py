import pandas as pd
import os

def trata_dados(caminho_estacao):
    if os.path.isfile(caminho_estacao):
        try:
            estacao_df = pd.read_csv(caminho_estacao, header=8, sep=';', encoding='latin-1')
        except Exception as e:
            raise e
    else:
        raise ValueError('Caminho não existente')
    
    lista_colunas_padrao = ['DATA (YYYY-MM-DD)', 'HORA (UTC)', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)', 
                            'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)', 'PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)', 
                            'PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)', 'RADIACAO GLOBAL (KJ/m²)', 
                            'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)', 'TEMPERATURA DO PONTO DE ORVALHO (°C)', 
                            'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)', 'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)', 
                            'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)', 'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)', 
                            'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)', 'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)', 
                            'UMIDADE RELATIVA DO AR, HORARIA (%)', 'VENTO, DIREÇÃO HORARIA (gr) (° (gr))', 
                            'VENTO, RAJADA MAXIMA (m/s)', 'VENTO, VELOCIDADE HORARIA (m/s)']
    
    # removendo colunas extras unnamed
    num_colunas = len(estacao_df.columns)
    num_colunas_padrao = len(lista_colunas_padrao)
    if num_colunas != num_colunas_padrao:
        try:
            estacao_df.drop(columns=estacao_df.columns[num_colunas_padrao:], inplace=True)
        except:
            raise ValueError('Erro ao remover colunas extras')
            
    
    
    
    # tratando coluna hora
    mask_utc = estacao_df['HORA (UTC)'].str.contains('UTC')  # mascara para pegar apenas os dados com UTC
    
    # trantando dados utc
    dados_utc = estacao_df.loc[mask_utc, 'HORA (UTC)']
    dados_utc = dados_utc.replace(' UTC', '', regex=True) # removendo UTC
    dados_utc = dados_utc.str[0:2] + ':00' # pegando apenas a hora

    # colocando os dados tratados no dataframe
    estacao_df.loc[mask_utc, 'HORA (UTC)'] = dados_utc.values


    # tratando coluna data
    estacao_df['DATA (YYYY-MM-DD)'] = estacao_df['DATA (YYYY-MM-DD)'].str.replace('/', '-')

    # criando DateTimeIndex a partir da coluna DATA (YYYY-MM-DD) e HORA (UTC)
    estacao_df_index = pd.to_datetime(estacao_df['DATA (YYYY-MM-DD)'] + ' ' + estacao_df['HORA (UTC)'])

    # removendo as colunas originais DATA (YYYY-MM-DD) e HORA (UTC)
    estacao_df.drop(['DATA (YYYY-MM-DD)', 'HORA (UTC)'], axis=1, inplace=True)

    # Define a coluna DATA HORA como índice
    estacao_df.set_index(estacao_df_index, inplace=True)


    # selecionando apenas as colunas usadas no plot
    estacao_df = estacao_df[['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)', 'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)']]

    # Transformando colunas de string para float
    estacao_df.replace(',', '.', regex=True, inplace=True)
    estacao_df = estacao_df.astype('float64')

    # tiranddo todos os possiveis valores nulos
    estacao_df.replace(['-9999', -9999, -9999.0, '-9999.0'], value= None, inplace=True)

    # preenchendo valores nulos
    estacao_df.bfill(inplace=True)
    
    return estacao_df