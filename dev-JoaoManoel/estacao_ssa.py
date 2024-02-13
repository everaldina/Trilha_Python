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

anos = r'2003|2013|2023'
links_csv = []

requisicao = requests.get(link, headers=headers)
resposta = bs4.BeautifulSoup(requisicao.text, 'html.parser')

lista = resposta.find('div', attrs={'id': 'main'}).find_all('a')

for item in lista:    
    if re.search(anos, item.contents[0]):
        links_csv.append(item.attrs['href'])
        
nomes = []
        
for link_csv in links_csv:
    nomes.append(link_csv.split('/')[-1])
    requisicao = requests.get(link_csv, headers=headers)
    
    if requisicao.status_code == 200:
        with open(link_csv.split('/')[-1], 'wb') as f:
            f.write(requisicao.content)
            print(f'Arquivo {link_csv.split("/")[-1]} salvo com sucesso!')
    else:
        print(f'Erro ao salvar o arquivo {link_csv.split("/")[-1]}')
    
for nome in nomes:
    with zipfile.ZipFile(nome, 'r') as zip_ref:
        zip_ref.extractall('estacao_ssa')
        print(f'Arquivo {nome} extraído com sucesso!')

estacao = '_SALVADOR_'
destino = 'data/'

if not os.path.exists(destino):
    os.makedirs(destino)

for root, dirs, files in os.walk('estacao_ssa'):
    for dir in dirs:
        for r, ds, fs in os.walk(dir):
            for f in fs:
                if estacao.lower() in f.lower():
                    shutil.move(f'{r}/{f}', destino)
                    print(f'Arquivo {f} movido com sucesso!')
                
    for file in files:
        if estacao.lower() in file.lower():
            shutil.move(f'{root}/{file}', destino)
            print(f'Arquivo {file} movido com sucesso!')
            
shutil.rmtree('estacao_ssa')
print('Pasta estacao_ssa removida com sucesso!')

for nome in nomes:
    os.remove(nome)
    print(f'Arquivo {nome} removido com sucesso!')

print('Fim do programa!')