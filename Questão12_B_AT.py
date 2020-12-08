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
  states = {
      'DF' : place[0].text,
      'GO' : place[1].text,
      'MT' : place[2].text,
      'MS' : place[3].text,
  }
  if state in states:
    return states[state]
  return f"Sigla digitada não pertence ao Centro-Oeste."
        


line()
state = str(input("Digite a sigla do Estado de consulta ('DF, GO, MT e MS'): ")).upper().strip()
line()
        
print(state_user(state))
