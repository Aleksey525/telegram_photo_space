import telegram
import os
from dotenv import load_dotenv
import random
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Скрипт для публикаций фотографий в телеграмм'
    )
    parser.add_argument('path', type=str, help='image_patc')
    parser.add_argument('--image_name', type=str, help='file_name')
    args = parser.parse_args()
    path = args.path
    file_name = args.image_name
    if file_name:
        file_path = f'{path}\{file_name}'
    else:
        names_files = [os.path.join(address, name).replace('//', '/')
                                         for address, dirs, files in os.walk(path) for name in files]
        file_path = f'{random.choice(names_files)}'
    load_dotenv()
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    chat_id = bot.get_updates()[-1].message.chat_id
    try:
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
    except telegram.error.NetworkError:
        print('Программа завершена')


if __name__ == '__main__':
    main()