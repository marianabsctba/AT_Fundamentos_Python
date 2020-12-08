#13) Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
A) Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
B) Conte quantas vezes apareceu a palavra ladies no conteúdo da página.


import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from functools import reduce

r = requests.get('http://brasil.pyladies.com/about')
r.encoding = 'utf-8'
file = r.text
soup = BeautifulSoup(file, "lxml")

whitelist = [
  'p'
]
text_elements = ''.join([t for t in soup.find_all(text=True) if t.parent.name in whitelist])

place = re.sub('[^a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]', '', text_elements).upper()


wordlist = place.split()
wordfreq = {}

for w in wordlist:
    wordfreq[w] = wordlist.count(w)

#print('Word Count')
#for w, ct in wordfreq.items():
#    print('{} {}'.format(w, ct))

distintas = len(wordfreq)
total = sum([ wordfreq[k] for k in wordfreq ])
print('Quantidade de ladies: {}'.format(wordfreq['LADIES']))
print(f'Quantidade de palavras distintas: {distintas}')
print(f'Total de palavras: {total}')
print('Palavras que apareceram somente uma vez')
for k in wordfreq:
  if wordfreq[k]==1:
    print(f'{k}')
