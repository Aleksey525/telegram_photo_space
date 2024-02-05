import telegram
import os
from dotenv import load_dotenv
import random
import argparse


def args_input(path, file_name):
    list_files = [os.path.join(address, name).replace('//', '/')
                  for address, dirs, files in os.walk(path) for name in files]
    if not file_name is None:
        return f'{path}\{file_name}'
    return f'{random.choice(list_files)}'


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    chat_id = bot.get_updates()[-1].message.chat_id
    file_path = args_input(path, file_name)
    bot.send_document(chat_id=chat_id, document=open(file_path, 'rb'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Скрипт для публикаций фотографий в телеграмм'
    )
    parser.add_argument('path', type=str, help='image_patc')
    parser.add_argument('--image_name', type=str, help='file_name')
    args = parser.parse_args()
    path = args.path
    file_name = args.image_name
    try:
        main()
    except telegram.error.NetworkError:
        print('Программа завершена')