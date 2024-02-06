import requests
from auxiliary_functions import image_download
import os
from dotenv import load_dotenv


def nasa_apod_foto(token):
    nasa_api = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token,
              'count': 30}
    response = requests.get(nasa_api, params=params)
    api_response = response.json()

    links_images = [link['url'] for link in api_response]
    directory = 'nasa_apod_images'
    for link in links_images:
        image_download(link, directory)


def main():
    load_dotenv()
    token = os.environ['API_TOKEN_NASA']
    try:
        nasa_apod_foto(token)
    except requests.exceptions.HTTPError:
        print('Программа завершена')


if __name__ == '__main__':
    main()