#12-B) ESCREVA UM PROGRAMA QUE OBTENHA DO USUÁRIO UMA SIGLA DO ESTADO DA REGIÃO CENTRO-OESTE E APRESENTA SUAS INFORMAÇÕES CORRESPONDENTES NA TABELA. 
# O RESULTADO DEVE APRESENTAR APENAS O CONTEÚDO, SEM FORMATAÇÃO. OU SEJA, AS TAGS NÃO DEVEM APARECER. NÃO ESQUEÇA DE CHECAR SE A SIGLA PERTENCE À REGIÃO.

import requests
from bs4 import BeautifulSoup

file = requests.get('https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html').text
soup = BeautifulSoup(file, "lxml")
place = soup.find_all('div', attrs={'class': 'linha'})

def line():
    print("==" * 30)

def state_user(state):
    if state == 'DF':
        return place[0].text
    elif state == 'GO':
        return place[1].text
    elif state == 'MT':
        return place[2].text
    elif state == 'MS':
        return place[3].text
    else:
        return f"Sigla digitada não existe."
    line()
        


line()
state = str(input("Digite a sigla do Estado de consulta ('DF, GO, MT e MS'): ")).upper().strip()
line()
        
print(state_user(state))
