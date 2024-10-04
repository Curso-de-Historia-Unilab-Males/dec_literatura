"""Script para coletar as imagens das capas dos livros que compõe a base de
dados.
"""
import pandas as pd
import requests
import os
import bs4
import wget

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://acervo.bn.gov.br",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}

data = input('Digite o caminho do arquivo csv: ')

# Carregar a base de dados
df = pd.read_csv(data, sep=';')

# Criar diretório para armazenar as imagens
if not os.path.exists('covers'):
    os.makedirs('covers')

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

# criar tupla de urls e titulo únicos
urls = [(row['arquivo'], row['título']) for i, row in df.iterrows()]

# function to clean titulo
def title_clean(title):
    title = title.lower()
    title = title.strip()
    title = title.replace(' ', '_')
    title = title.replace('/', '_')
    title = title.replace(':', '_')
    title = title.replace('?', '_')
    title = title.replace('!', '_')
    title = title.replace(';', '_')
    title = title.replace(',', '_')
    title = title.replace('(', '_')
    title = title.replace(')', '_')
    title = title.replace('[', '_')
    title = title.replace(']', '_')
    title = title.replace('{', '_')
    title = title.replace('}', '_')
    title = title.replace('"', '_')
    title = title.replace("'", '_')
    # truncate title
    if len(title) > 30:
        title = title[:30]
    return title
# Iterar sobre as tuplas urls
# baixar as imagens e salvar no diretório 'capas' com o nome do titulo
for url, titulo in urls:
    titulo = title_clean(titulo)
    print(titulo)
    # check if image is already downloaded
    if os.path.exists(f'covers/{titulo}.jpg'):
        print(f'A imagem {titulo}.jpg já foi baixada')
        continue
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        with open(f'covers/{titulo}.jpg', 'wb') as f:
            f.write(response.content)
        print(f'Imagem {titulo}.jpg baixada com sucesso.')
    except Exception as e:
        print(f'Erro {url}: {e}\n')
