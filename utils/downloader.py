import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
import re
from tqdm import tqdm



def download_site(url, output_dir, logger, file_types):
    logger.info(f"Démarrage du téléchargement pour : {url}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"path not exists : {output_dir}")
        logger.info(f"creat path : {output_dir}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

      
        main_page = os.path.join(output_dir, "index.html")
        with open(main_page, "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        logger.info(f"Page principale enregistrée : {main_page}")

       
        resources = []
        for tag, attr in [("link", "href"), ("script", "src"), ("img", "src")]:
            for resource in soup.find_all(tag):
                if attr in resource.attrs:
                    resource_url = urljoin(url, resource[attr])
                    if any(resource_url.endswith(f".{ext}") for ext in file_types):
                        resources.append(resource_url)

        print(f"\n🔄 Téléchargement de {len(resources)} ressources associées :\n")
        for resource_url in tqdm(resources, desc="Téléchargement des ressources", unit="fichier"):
            download_resource(resource_url, output_dir, logger)

    except requests.RequestException as e:
        logger.error(f"Erreur de requête : {e}")
        raise
    logger.info("Téléchargement terminé.")




def download_resource(resource_url, output_dir, logger):
    try:
        logger.info(f"Téléchargement de la ressource : {resource_url}")
        response = requests.get(resource_url, stream=True)
        response.raise_for_status()

        parsed_url = urlparse(resource_url)
        filename = os.path.basename(parsed_url.path)
        if not filename or "?" in filename or "&" in filename:
            filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', parsed_url.path)
        filename = filename[:255]



        file_path = os.path.join(output_dir, filename)

      
        total_size = int(response.headers.get('content-length', 0))
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        logger.info(f"Ressource téléchargée avec succès : {file_path}")
    except requests.RequestException as e:
        logger.warning(f"Échec du téléchargement : {resource_url} - {e}")
    except Exception as e:
        logger.error(f"Erreur lors du téléchargement : {e}")
