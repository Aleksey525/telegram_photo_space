import os
import requests
from urllib.parse import urlsplit, unquote


def get_file_name(file_link):
    splited_link = urlsplit(file_link)
    file_path = unquote(splited_link.path)
    splited_file_path = os.path.split(file_path)
    file_name = splited_file_path[1]
    return file_name


def image_download_with_params(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    os.makedirs(path, exist_ok=True)
    path_template = f'{path}/{get_file_name(url)}'
    with open(path_template, 'wb') as file:
        file.write(response.content)