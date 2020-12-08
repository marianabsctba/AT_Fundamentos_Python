#11) OBTENHA, USANDO REQUESTS OU URLLIB, DENTRO DE SEU PROGRAMA EM PYTHON, O CSV DO LINK:
#HTTPS://SITES.GOOGLE.COM/SITE/DR2FUNDAMENTOSPYTHON/ARQUIVOS/VIDEO_GAMES_SALES_AS_AT_22_DEC_2016.CSV
#OBTENHA, DENTRE OS JOGOS DO GÊNERO DE AÇÃO (ACTION), TIRO (SHOOTER) E PLATAFORMA (PLATFORM):
#QUAIS SÃO AS TRÊS MARCAS QUE MAIS PUBLICARAM JOGOS DOS TRÊS GÊNEROS COMBINADOS? INDIQUE TAMBÉM O TOTAL DE JOGOS DE CADA MARCA.
#QUAIS SÃO AS TRÊS MARCAS QUE MAIS VENDERAM OS TRÊS GÊNEROS COMBINADOS? INDIQUE TAMBÉM O TOTAL DE VENDAS DE CADA MARCA.
#QUAL É A MARCA COM MAIS PUBLICAÇÕES EM CADA UM DOS GÊNEROS NOS ÚLTIMOS DEZ ANOS NO JAPÃO? INDIQUE TAMBÉM O NÚMERO TOTAL DE JOGOS DELA.
#QUAL FOI A MARCA QUE MAIS VENDEU EM CADA UM DESSES GÊNEROS NOS ÚLTIMOS DEZ ANOS, NO JAPÃO? INDIQUE TAMBÉM O TOTAL DE VENDAS DELA.

import requests, csv, pandas as pd

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename



def filter_genres(data_frame):
    return  data_frame[ (data_frame['Genre'] == 'Action') |
                        (data_frame['Genre'] == 'Shooter') |
                        (data_frame['Genre'] == 'Platform') ]



file =  download_file('https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv')


dt_frame = pd.read_csv(file, sep=',')
frame_genre = dt_frame[ (dt_frame['Genre'] == 'Action') |
                        (dt_frame['Genre'] == 'Shooter') |
                        (dt_frame['Genre'] == 'Platform') ]

agg_dt_frame = frame_genre.groupby(['Publisher']).agg({'Publisher': ['count'], 'Global_Sales': ['sum']})

    
print('********  Questão A  **********')
print('MAIS PUBLICARAM -  JOGOS (TOTAL) - VENDAS (TOTAL)')
print(agg_dt_frame
    .sort_values(ascending=False, by=('Publisher', 'count'))
    .head(3))
print('******************\n')



print('********  Questão B  **********')
print('MAIS VENDERAM  -  JOGOS(TOTAL)  -  VENDAS (TOTAL)')
print(agg_dt_frame
    .sort_values(ascending=False, by=('Global_Sales', 'sum'))
    .head(3))
print('******************\n')


jp_data_Frame = frame_genre[ (frame_genre['JP_Sales'] > 0) &  (frame_genre['Year_of_Release'] >= 2010)  ]
  

print('********  Questão C  **********')
print('GÊNERO - MAIS PUBLICAÇÕES (JAPÃO) -  TOTAL DE JOGOS')
counted = jp_data_Frame.groupby(['Genre', 'Publisher']).agg(['count'])
g = counted[('Name','count')].groupby('Genre', group_keys=False)
print(g.nlargest(1))

print('********   Questão D  **********')
print('MAIS VENDAS (JAPÃO)')

dt_japan_c = jp_data_Frame[(jp_data_Frame['Genre']) == "Action" ].groupby(['Publisher', 'Genre'])['JP_Sales'].agg(['sum']).sort_values(ascending=False, by='sum').head(1)

dt_japan_c = dt_japan_c.append(jp_data_Frame[ (jp_data_Frame['Genre']) == "Shooter" ]
    .groupby(['Publisher', 'Genre'])['JP_Sales'].agg(['sum'])
    .sort_values(ascending=False, by='sum')
    .head(1))

dt_japan_c = dt_japan_c.append(jp_data_Frame[ (jp_data_Frame['Genre']) == "Platform" ]
    .groupby(['Publisher', 'Genre'])['JP_Sales'].agg(['sum'])
    .sort_values(ascending=False, by='sum')
    .head(1))    


total_jogos = jp_data_Frame.groupby(['Publisher'])['JP_Sales'].agg(['sum']).rename(columns={'sum': 'Total de vendas'})


print(pd.merge(dt_japan_c, total_jogos, left_on='Publisher', right_on='Publisher', how='left'))
print('******************\n')
