import os
import pandas as pd

# Carregar a base de dados original
df = pd.read_csv('full_data.csv', sep=';')

# Função para limpar e normalizar o título (mantendo a mesma lógica de nomeação de arquivos)
def title_clean(title):
    title = title.lower().strip()
    title = title.replace(' ', '_').replace('/', '_').replace(':', '_')
    title = title.replace('?', '_').replace('!', '_').replace(';', '_')
    title = title.replace(',', '_').replace('(', '_').replace(')', '_')
    title = title.replace('[', '_').replace(']', '_').replace('{', '_')
    title = title.replace('}', '_').replace('"', '_').replace("'", '_')
    if len(title) > 30:
        title = title[:30]
    return title

# Limpar e normalizar os títulos
df['cleaned_titulo'] = df['título'].apply(title_clean)

# Verificar os arquivos já baixados no diretório 'covers'
downloaded_files = set(os.listdir('../get_images/covers'))  # Lista de arquivos já baixados

# Criar uma nova coluna com os links permanentes baseados nos arquivos existentes
base_url = f'https://raw.githubusercontent.com/Curso-de-Historia-Unilab-Males/dec_literatura/refs/heads/main/data/get_images/covers/'

# Mapear os arquivos existentes para as URLs
def get_cover_url(cleaned_title):
    file_name = f'{cleaned_title}.jpg'
    if file_name in downloaded_files:
        return base_url + file_name
    else:
        return 'Imagem não disponível'

df['cover_url'] = df['cleaned_titulo'].apply(get_cover_url)

# delete "" from the column 'título'
df['título'] = df['título'].str.replace('"', '')
df['título'] = df['título'].str.replace(';', ',')

# Salvar a base de dados atualizada com as URLs das capas
df.to_csv('base_atualizada_com_capas.csv', sep=';', index=False)
print("Base de dados atualizada com URLs das capas gerada com sucesso!")

