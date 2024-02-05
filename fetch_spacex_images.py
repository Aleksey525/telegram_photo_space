import requests
import argparse
from auxiliary_functions import image_download


def fetch_spacex_last_launch(id=None):
    url_api = 'https://api.spacexdata.com/v5/launches/{}'
    if id is None:
        complite_url = url_api.format('latest')
    else:
        complite_url = url_api.format(id)
    response = requests.get(complite_url)
    response.raise_for_status()
    link_list = response.json()['links']['flickr']['original']
    directory = 'images_spacex'
    if len(link_list) == 0:
        print('Фотографий последнего запуска не обнаружено, попробуйте поиск по id')
    else:
        for link in link_list:
            image_download(link, directory)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Скрипт для скачивания фотографий запусков SpaceX'
    )
    parser.add_argument('--id', type=str, help='launch id')
    args = parser.parse_args()
    try:
        fetch_spacex_last_launch(args.id)
    except requests.exceptions.HTTPError:
        print('Программа завершена')