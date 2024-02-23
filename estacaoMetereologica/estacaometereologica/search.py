import requests
import bs4

class Search:
    def __init__(self):
        self.link = 'https://portal.inmet.gov.br/dadoshistoricos'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        try:
            self.requisicao = requests.get(self.link, headers=self.headers)
        except ConnectionError:
            self.requisicao = None
            self.resposta = None
            raise Exception('Requisição não foi bem sucedida')
        except Exception as e:
            self.requisicao = None
            self.resposta = None
            raise e
        if self.requisicao:
            self.resposta = bs4.BeautifulSoup(self.requisicao.text, 'html.parser')
        else:
            self.resposta = None
    
    def get_anos(self):
        if self.resposta:
            lista_anos = {}
            lita_links = self.resposta.find('div', attrs={'id': 'main'}).find_all('a')
            for item in lita_links:
                link = item.attrs['href']
                ano = link.split('/')[-1]
                lista_anos[ano[:-4]] =  link # Adiciona tupla com o ano e o link do arquivo .zip
            return lista_anos
        else:
            raise Exception('Requisição não foi bem sucedida')