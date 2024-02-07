import requests
import pandas as pd

def buscaML(query):
    url = "https://api.mercadolibre.com/sites/MLB/search?"
    url = url + "q=" + query
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['results'])
    return df

def main():
    print(buscaML("iphone"))
    
    
if __name__ == "__main__":
    main()