# Projeto de Download Automático de Arquivos .zip

Este projeto é um script Python que faz o download automático de arquivos `.zip` de um site. Ele usa bibliotecas como `requests`, `BeautifulSoup` e `tqdm` para buscar e baixar os arquivos, exibindo uma barra de progresso durante o processo de download.

O projeto foi inspirado no site https://class.devsamurai.com.br/ que disponibilizou todo seu acervo para download. Os arquivos baixados podem estar sujeitos à restrições de direitos autorais, mas seu uso para fins pessoais é totalmente gratuito.

## Funcionalidades

- Requisição a um site para obter links de arquivos `.zip`.
- Filtragem de links que terminam com `.zip`.
- Download automático de arquivos com a exibição de uma barra de progresso.
- Salvamento dos arquivos no diretório de execução do script.

## Pré-requisitos

Antes de rodar o script, você precisa ter o Python instalado na sua máquina e as dependências necessárias.

### Instalação do Python

Caso você ainda não tenha o Python instalado, baixe e instale a versão mais recente de [python.org](https://www.python.org/).

### Criar um ambiente virtual
É uma boa prática usar um ambiente virtual para evitar conflitos com o sistema. Você pode criar um ambiente virtual com os seguintes comandos:
```bash
python -m venv myenv
source myenv/bin/activate  # No Linux/macOS
myenv\Scripts\activate     # No Windows
pip install requests beautifulsoup4
```
Depois de ativar o ambiente virtual, os pacotes serão instalados nesse ambiente e não afetarão o Python global do sistema.

### Dependências

Você precisará instalar as seguintes bibliotecas Python:

- `requests`: para fazer requisições HTTP.
- `beautifulsoup4`: para parsear o HTML da página e extrair links.
- `tqdm`: para exibir a barra de progresso durante o download.

Para instalar as dependências, rode o seguinte comando:

```bash
pip install requests beautifulsoup4 tqdm
```

### Como Usar
Passo 1: Clonar o repositório
Clone o repositório para a sua máquina local:
```bash
git clone https://github.com/oMaestro174/samurai-downloader.git
```
Passo 2: Rodar o Script
Entre no diretório do projeto e execute o script:

```bash
cd samurai-downloader
python samurai-downloader.py
```
O script vai baixar todos os arquivos .zip encontrados no site e salvar na mesma pasta onde o script foi executado.
Personalizando o URL
Se você precisar usar um URL diferente, modifique o valor da variável site_url no código:

```python
site_url = 'https://class.devsamurai.com.br/'  # Substitua com a URL desejada
```
Personalizando o Diretório de Download
Os arquivos serão salvos no diretório onde o script foi executado, mas você pode personalizar isso alterando o valor de download_path no código:
```python
download_path = '/caminho/para/o/diretorio'
```

### Explicação do Código
Requisição e Parsing: O script faz uma requisição à URL fornecida e utiliza o BeautifulSoup para extrair todos os links de arquivos .zip.
Filtragem dos Links: Apenas os links que terminam com .zip são considerados.
Download com Barra de Progresso: O arquivo é baixado em pedaços (chunks) e a barra de progresso é exibida usando a biblioteca tqdm.
Exemplo de Saída
Durante o download dos arquivos, você verá algo assim no terminal:

```bash
Baixando: Aulas ao Vivo.zip
Baixando: Backend - Dominando o NodeJS.zip
```
E a barra de progresso aparecerá como:
```bash
Baixando: Aulas ao Vivo.zip: 100%|███████████████████████████████| 10.2M/10.2M [00:04<00:00, 2.45MB/s]
```
Licença
Este projeto está licenciado sob a Licença MIT.
