import pandas as pd
from urllib.parse import quote

# Carregar o arquivo CSV
df = pd.read_csv('base_atualizada_com_capas.csv', sep=';')

# Função para codificar as URLs
def encode_url(url):
    return quote(url, safe=':/')

# Aplicar a função de codificação na coluna 'cover_url'
df['cover_url'] = df['cover_url'].apply(encode_url)

# Salvar o CSV atualizado
df.to_csv('base_atualizada_com_capas_codificada.csv', sep=';', index=False)

print("URLs codificadas e CSV atualizado salvo com sucesso!")

