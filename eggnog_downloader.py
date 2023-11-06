
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
import time
import re

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def is_safe_path(basedir, path, follow_symlinks=True):
    # Resolve symbolic links
    if follow_symlinks:
        return os.path.realpath(path).startswith(basedir)
    return os.path.abspath(path).startswith(basedir)

def get_user_input():
    while True:
        url = input('Insira o link do resultado do Eggnog: ')
        if is_valid_url(url):
            break
        print("URL inválido, tente novamente.")
    download_dir = input('Insira o caminho da pasta de destino para salvar os arquivos: ')
    sample_id = input('Insira um identificador para a amostra: ')
    sample_id = re.sub(r'[^a-zA-Z0-9_-]', '_', sample_id)  # Remove caracteres não seguros
    return url, download_dir, sample_id

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    elif not os.path.isdir(directory):
        raise Exception(f"O caminho {directory} existe e não é um diretório.")

def fetch_page(url):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'})
    try:
        response = session.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Ocorreu um erro ao buscar a página: {e}')
        raise
    else:
        return BeautifulSoup(response.text, 'html.parser')

def download_file(session, url, download_dir, sample_id, file_name):
    file_path = os.path.join(download_dir, f"{sample_id}_{file_name}")
    if os.path.exists(file_path):
        print(f"O arquivo {file_name} já existe e não será sobrescrito.")
        return
    try:
        response = session.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'Arquivo baixado com sucesso: {file_path}')
    except requests.RequestException as e:
        print(f'Erro ao baixar o arquivo: {e}')
        if os.path.exists(file_path):
            os.remove(file_path)  # Remove o arquivo parcialmente baixado

def download_files(soup, url, download_dir, sample_id, file_list):
    session = requests.Session()
    links = soup.find_all('a', href=True)
    found_files = {file_name: False for file_name in file_list}
    for link in links:
        for file_name in file_list:
            if file_name in link['href']:
                found_files[file_name] = True
                file_url = urljoin(url, link['href'])
                
                download_file(session, file_url, download_dir, sample_id, file_name)
                break
    for file_name, found in found_files.items():
        if not found:
            print(f'Arquivo "{file_name}" não encontrado na página fornecida.')

# Lista dos nomes dos arquivos a serem baixados
file_list = [
    "emapper.err",
    "emapper.out",
    "info.txt",
    "out.emapper.annotations.xlsx",
    "out.emapper.decorated.gff",
    "out.emapper.genepred.fasta",
    "out.emapper.genepred.gff",
    "out.emapper.hits",
    "out.emapper.orthologs",
    "out.emapper.annotations",
    "out.emapper.seed_orthologs",
    "queries.fasta",
    "queries.raw"
]

if __name__ == '__main__':
    url, download_dir, sample_id = get_user_input()
    create_directory(download_dir)
    soup = fetch_page(url)
    if soup:
        download_files(soup, url, download_dir, sample_id, file_list)
