import requests
from auxiliary_functions import image_download_with_params
import os
from dotenv import load_dotenv


def fetch_nasa_apod_photos(token):
    nasa_api_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token,
              'count': 30}
    response = requests.get(nasa_api_url, params=params)
    api_response = response.json()
    images_links = [link['url'] for link in api_response]
    directory = 'nasa_apod_images'
    for link in images_links:
        image_download_with_params(link, directory, params)


def main():
    load_dotenv()
    token = os.environ['API_TOKEN_NASA']
    try:
        fetch_nasa_apod_photos(token)
    except requests.exceptions.HTTPError:
        print('Программа завершена')


if __name__ == '__main__':
    main()