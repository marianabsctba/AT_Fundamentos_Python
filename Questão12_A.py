#12-A IMPRIMA O CONTEÚDO REFERENTE APENAS À TABELA APRESENTADA NA PÁGINA INDICADA.

import pandas as pd
import requests
from bs4 import BeautifulSoup


file = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
html = requests.get(file).text
soup = BeautifulSoup(html, "lxml")

def printle():   
    for tabela in soup.find_all('div', class_='tabela'):
        return tabela.text


print(printle())
