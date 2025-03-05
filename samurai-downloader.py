import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote
from tqdm import tqdm

# Defina a URL do site onde os arquivos estão
site_url = 'https://class.devsamurai.com.br/'  # Substitua pela URL correta

# Defina o diretório onde os arquivos serão salvos
download_path = r'D:\samurai-downloader-main\cursos-samurai'

# Garante que o diretório de download existe
os.makedirs(download_path, exist_ok=True)

# Faça a requisição à página
response = requests.get(site_url)
if response.status_code != 200:
    print("Erro ao acessar o site.")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Encontre todos os links da página
links = soup.find_all('a', href=True)

# Filtrar links válidos que terminam com .zip
zip_links = [urljoin(site_url, link['href']) for link in links if '.zip' in link['href']]

if not zip_links:
    print("Nenhum arquivo .zip encontrado.")
    exit()

# Baixar os arquivos .zip encontrados
for link in zip_links:
    file_name = unquote(link.split('/')[-1].split('?')[0])  # Remove parâmetros da URL
    file_path = os.path.join(download_path, file_name)

    # Verifica se o arquivo já foi baixado e seu tamanho
    existing_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0

    # Obtém o tamanho total do arquivo no servidor
    head = requests.head(link)
    total_size = int(head.headers.get('Content-Length', 0))

    if existing_size >= total_size:
        print(f"Arquivo já baixado: {file_name}")
        continue  # Pula para o próximo arquivo

    print(f"\nBaixando: {file_name}")

    headers = {"Range": f"bytes={existing_size}-"} if existing_size > 0 else {}

    with requests.get(link, headers=headers, stream=True) as r:
        r.raise_for_status()

        with open(file_path, 'ab') as f, tqdm(
            total=total_size,
            initial=existing_size,
            unit='B',
            unit_scale=True,
            desc=file_name
        ) as progress:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                progress.update(len(chunk))

print("\nDownload concluído!")
