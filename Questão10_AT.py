#10) OBTENHA, USANDO REQUESTS OU URLLIB, DENTRO DE SEU PROGRAMA EM PYTHON, O CSV DO LINK:
#HTTPS://SITES.GOOGLE.COM/SITE/DR2FUNDAMENTOSPYTHON/ARQUIVOS/WINTER_OLYMPICS_MEDALS.CSV
#E:
#DENTRE OS SEGUINTES PAÍSES NÓRDICOS: SUÉCIA, DINAMARCA E NORUEGA, VERIFIQUE: NO SÉCULO XXI (A PARTIR DE 2001), QUAL FOI O MAIOR MEDALHISTA DE OURO, CONSIDERANDO APENAS AS SEGUINTES MODALIDADES:
#CURLING
#PATINAÇÃO NO GELO (SKATING)
#ESQUI (SKIING)
#HÓQUEI SOBRE O GELO (ICE HOCKEY)
#PARA CADA ESPORTE, CONSIDERE TODAS AS MODALIDADES, TANTO NO MASCULINO QUANTO NO FEMININO. SUA RESPOSTA DEVE IMPRIMIR UM RELATÓRIO MOSTRANDO O TOTAL DE MEDALHAS DE CADA UM DOS PAÍSES E EM QUE ESPORTE, ANO, CIDADE E GÊNERO (MASCULINO OU FEMININO) CADA MEDALHA FOI OBTIDA.

import requests, csv, pandas as pd

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename



file =  download_file('https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv')



dt_frame = pd.read_csv(file, sep=',')
dt_paises = dt_frame[(dt_frame['NOC'] == 'SWE') | 
                     (dt_frame['NOC'] == 'DEN') | 
                     (dt_frame['NOC'] == 'NOR')]

dt_filtra_ano = dt_paises[(dt_paises['Year'] > 2000)]

dt_filtrado_esportes = dt_filtra_ano[(dt_filtra_ano['Sport'] == 'Curling') |
                       (dt_filtra_ano['Sport'] == 'Skating') |
                       (dt_filtra_ano['Sport'] == 'Skiing') | 
                       (dt_filtra_ano['Sport'] == 'Ice Hockey')]



print('**** Questão A ********')
dt_curling = dt_filtrado_esportes[(dt_filtrado_esportes['Sport'] == 'Curling') &
             (dt_filtrado_esportes['Medal'] == 'Gold')]

dt_curling.groupby(['NOC'])['NOC'].count()

print('**** Curling ********')
print('--- MAIOR MEDALISTA DE OURO ---')
print(dt_curling.groupby(['NOC'])['NOC'].count())
print('***************\n')

dt_skating = dt_filtrado_esportes[(dt_filtrado_esportes['Sport'] == 'Skating') & 
            (dt_filtrado_esportes['Medal'] == 'Gold')]

print('**** Skating ********')
print('--- MAIOR MEDALISTA DE OURO --- (NENHUM RESULTADO ENCONTRADO)')
print(dt_skating.groupby(['NOC'])['NOC'].count())
print('***************\n')

dt_skiing = dt_filtrado_esportes[(dt_filtrado_esportes['Sport'] == 'Skiing') & 
            (dt_filtrado_esportes['Medal'] == 'Gold')]

print('**** Skiing ********')
print('--- MAIOR MEDALISTA DE OURO ---')
print(dt_skiing.groupby(['NOC'])['NOC'].count())
print('***************\n')

dt_ice_hockey = dt_filtrado_esportes[(dt_filtrado_esportes['Sport'] == 'Ice Hockey') & 
                (dt_filtrado_esportes['Medal'] == 'Gold')]

print('**** Ice Hockey *******')
print('--- MAIOR MEDALISTA DE OURO ---')
print(dt_ice_hockey.groupby(['NOC'])['NOC'].count())
print('***************\n')


print('******* Questão B **************')
print('---- RELATÓRIO DA QUANTIDADE DE MEDALHAS POR PAÍS, ESPORTE, ANO, CIDADE E SEXO ----')
q_b= dt_frame.groupby(['NOC', 'Sport', 'Year','City','Event gender'])[['Medal']].count()

print(q_b)
q_b.to_html('report.html')
print('**********************\n')
