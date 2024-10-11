import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('base_atualizada_com_capas_codificada.csv', sep=';')

# Passo 1: Filtrar as linhas onde a coluna 'cover_url' possui 'Imagem não disponível'
df_missing_images = df[df['cover_url'] == 'Imagem%20n%C3%A3o%20dispon%C3%ADvel']

# copiar valores de coluna 'arquivo' para 'cover_url'
df_missing_images['cover_url'] = df_missing_images['arquivo']

# Salvar essas linhas em um novo arquivo CSV
df_missing_images.to_csv('itens_sem_imagem.csv', sep=';', index=False)
