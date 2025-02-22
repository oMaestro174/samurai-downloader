import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote
from tqdm import tqdm  # Importando a biblioteca tqdm

# Defina a URL do site onde os arquivos estão
site_url = 'https://class.devsamurai.com.br/'  # Substitua com a URL correta

# Defina o diretório onde os arquivos serão salvos
download_path = os.getcwd()  # ou substitua por um diretório específico, como '/caminho/para/pasta'

# Faça a requisição à página
response = requests.get(site_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontre todos os links de arquivos .zip na página
links = soup.find_all('a', href=True)

# Filtre os links que terminam com '.zip'
zip_links = [urljoin(site_url, link['href']) for link in links if link['href'].endswith('.zip')]

# Baixe cada arquivo .zip
for link in zip_links:
    # Extraia o nome do arquivo do link e decodifique o nome
    file_name = unquote(link.split('/')[-1])
    file_path = os.path.join(download_path, file_name)
    print(f"Baixando: {file_name}")

    # Baixe o arquivo com barra de progresso
    with requests.get(link, stream=True) as r:
        r.raise_for_status()

        # Pegue o tamanho total do arquivo (caso esteja disponível)
        total_size = int(r.headers.get('Content-Length', 0))

        # Inicialize a barra de progresso
        with open(file_path, 'wb') as f:
            # Use tqdm para exibir a barra de progresso
            for chunk in tqdm(r.iter_content(chunk_size=8192), total=total_size // 8192, unit='B', unit_scale=True):
                f.write(chunk)

print("Download concluído!")
