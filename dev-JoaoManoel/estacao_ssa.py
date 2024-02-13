import requests
import zipfile
import shutil
import bs4
import re
import os

link = 'https://portal.inmet.gov.br/dadoshistoricos'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

anos = r'2003|2013|2023'                # Anos desejados
links_csv = []                          # Lista de links para os arquivos .csv
nomes_arquivos = []                     # Lista de nomes dos arquivos .zip
estacao = '_SALVADOR_'                  # Nome da estação desejada (entre _ para evitar conflitos com outras estações da mesma cidade)
pasta_destino = 'data/'                 # Pasta de destino dos arquivos .csv

requisicao = requests.get(link, headers=headers)
resposta = bs4.BeautifulSoup(requisicao.text, 'html.parser')

lista = resposta.find('div', attrs={'id': 'main'}).find_all('a')    # Lista de tags <a> que possuem os links para download dos arquivos .zip

for item in lista:    
    if re.search(anos, item.contents[0]):       # Verifica se o link é de um dos anos desejados por regex
        links_csv.append(item.attrs['href'])    # Adiciona o link do arquivo .zip à lista de links
        
for link_csv in links_csv:      # Faz o download dos arquivos .zip
    nomes_arquivos.append(link_csv.split('/')[-1])
    
    requisicao = requests.get(link_csv, headers=headers)
    
    if requisicao.status_code == 200:
        with open(link_csv.split('/')[-1], 'wb') as f:
            f.write(requisicao.content)
            print(f'Arquivo {link_csv.split("/")[-1]} salvo com sucesso!')
    else:
        print(f'Erro ao salvar o arquivo {link_csv.split("/")[-1]}')
    
for nome in nomes_arquivos:     # Extrai os arquivos .zip
    with zipfile.ZipFile(nome, 'r') as zip_ref:
        zip_ref.extractall('estacao_ssa')
        print(f'Arquivo {nome} extraído com sucesso!')

# Se a pasta de destino não existir, cria a pasta
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Move os arquivos .csv para a pasta de destino
for root, dirs, files in os.walk('estacao_ssa'):
    # Move os arquivos que estão dentro de subpastas
    for dir in dirs:
        for r, ds, fs in os.walk(dir):
            for f in fs:
                if estacao.lower() in f.lower():
                    shutil.move(f'{r}/{f}', pasta_destino)
                    print(f'Arquivo {f} movido com sucesso!')
    
    # Move os arquivos que estão na pasta raiz    
    for file in files:
        if estacao.lower() in file.lower():
            shutil.move(f'{root}/{file}', pasta_destino)
            print(f'Arquivo {file} movido com sucesso!')

# Remove os arquivos .zip e a pasta estacao_ssa
shutil.rmtree('estacao_ssa')
print('Pasta estacao_ssa removida com sucesso!')

for nome in nomes_arquivos:
    os.remove(nome)
    print(f'Arquivo {nome} removido com sucesso!')