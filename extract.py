from extracts.itemsadder import ItemsAdder
from extracts.nexo import Nexo
from utils import Utils
import os
import requests
import zipfile

if os.path.exists(".env"):
    import dotenv
    dotenv.load_dotenv()

def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)

if os.getenv("download_url"):
    download_file(os.getenv("download_url"), "Content.zip")

with zipfile.ZipFile("Content.zip", "r") as zip_ref:
    zip_ref.extractall("pack")
os.remove("Content.zip")

if all(os.path.exists(path) for path in ("ItemsAdder/contents", "ItemsAdder/storage/items_ids_cache.yml")):
    ItemsAdder().extract()

if all(os.path.exists(path) for path in ("pack/Nexo/items", "pack/Nexo/pack")):
    Nexo().extract()

print("Done")