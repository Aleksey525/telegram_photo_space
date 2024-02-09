import requests
import argparse
from auxiliary_functions import image_download_with_params


def fetch_spacex_last_launch(launch_id):
    url_api = 'https://api.spacexdata.com/v5/launches/{}'
    complite_url = url_api.format(launch_id)
    response = requests.get(complite_url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    directory = 'images_spacex'
    if not links:
        print('Фотографий последнего запуска не обнаружено, попробуйте поиск по id')
    else:
        for link in links:
            image_download_with_params(link, directory)


def main():
    parser = argparse.ArgumentParser(
        description='Скрипт для скачивания фотографий запусков SpaceX'
    )
    parser.add_argument('--launch_id', default='latest', type=str, help='launch id')
    args = parser.parse_args()
    try:
        fetch_spacex_last_launch(args.launch_id)
    except requests.exceptions.HTTPError:
        print('Программа завершена')


if __name__ == '__main__':
    main()
