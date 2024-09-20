"""Script para coletar as imagens das capas dos livros que compõe a base de
dados.
"""
import pandas as pd
import requests
import os
import bs4
import wget

# Carregar a base de dados
df = pd.read_csv('cult-mit-africa.csv')

# Criar diretório para armazenar as imagens
if not os.path.exists('capas'):
    os.makedirs('capas')

# renomear colunas: remover espaços antes do nome e colocar em minúsculo
df.columns = [col.lower().strip() for col in df.columns]

# caso colçuna arrquivo posuua valores nulos, preencher com 'None'
df['arquivo'].fillna('None', inplace=True)

# Iterar sobre as linhas da base de dados na coluna 'arquivo'
# caso item poussua a string 'acesse.one' ou 'l1nk.dev' excluir
list_drop = ['acesse.one', 'l1nk.dev', 'None', 'github.com']
for i, row in df.iterrows():
    for item in list_drop:
        if item in row['arquivo']:
            df.drop(i, inplace=True)

# criar tupla de urls e identificadores únicos
urls = [(row['arquivo'], row['identificador']) for i, row in df.iterrows()]

# Iterar sobre as tuplas urls
# baixar as imagens e salvar no diretório 'capas' com o nome do identificador
for url, identificador in urls:
    if url.endswith('.jpg'):
        print(f'Baixando a imagem {url} com método requests')
        response = requests.get(url)
        response.raise_for_status()
        try:
            with open(f'capas/{identificador}.jpg', 'wb') as f:
                f.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f'Erro ao baixar a imagem {url}: {e}')
    else:
        print(f'Baixando a imagem {url} com método bs4')
        # use bs4 para extrair a url da imagem
        try:
            response = requests.get(url)
            # response.raise_for_status()
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            img = soup.find('img')
            img_url = img['src']
            # use wget para baixar a imagem
            wget.download(img_url, f'capas/{identificador}.jpg')
        except requests.exceptions.RequestException as e:
            print(f'Erro ao baixar a imagem {url}: {e}')
        except (KeyError, TypeError) as e:
            print(f'Erro ao extrair a url da imagem {url}: {e}')
        except Exception as e:
            print(f'Erro desconhecido: {e}')
