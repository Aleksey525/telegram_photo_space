import requests
from auxiliary_functions import image_download
import os
from dotenv import load_dotenv
import datetime


def nasa_epic_foto(token):
    template = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png?api_key={}'
    api_epic = 'https://api.nasa.gov/EPIC/api/natural/images?'
    params = {'api_key': token}
    response = requests.get(api_epic, params=params)
    api_response = response.json()
    directory = 'images_epic_nasa'
    for event in api_response:
        date = datetime.datetime.fromisoformat(event['date'])
        format_date = date.strftime('%Y/%m/%d')
        complete_api = template.format(format_date, event['image'], token)
        image_download(complete_api, directory)


def main():
    load_dotenv()
    token = os.environ['API_TOKEN_NASA']
    try:
        nasa_epic_foto(token)
    except requests.exceptions.HTTPError:
        print('Программа завершена')


if __name__ == '__main__':
    main()