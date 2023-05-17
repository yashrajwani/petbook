import pandas as pd
import numpy as np
import re
import os
import requests 
import zipfile 
import tarfile


data_path = "/app/"
DATA_URL = "https://storage.googleapis.com/petbook-project-data/raw_data/persistent-folder.zip"

def download_file(packet_url, base_path="", extract=False, headers=None):
    if base_path != "":
        if not os.path.exists(base_path):
            os.mkdir(base_path)
    packet_file = os.path.basename(packet_url)
    with requests.get(packet_url, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(os.path.join(base_path, packet_file), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Data downloaded {packet_file}")

    if extract:
        if packet_file.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(base_path, packet_file)) as zfile:
                zfile.extractall(base_path)
            print(os.listdir(base_path))
            print(os.listdir(data_path))
            
        else:
            packet_name = packet_file.split('.')[0]
            with tarfile.open(os.path.join(base_path, packet_file)) as tfile:
                tfile.extractall(base_path)
        print("File Extracted")

# # ensure that the data is loaded into the disk
def ensure_data_loaded():
    try:
        print("ensure_data_loaded()")
        if not os.path.exists(data_path+"/persistent-folder"):
            print("Downloading...")
            download_file(DATA_URL, base_path=data_path, extract=True)
        else:
            print(data_path, "is available")

        

    except Exception as exc:
        print(str(exc))