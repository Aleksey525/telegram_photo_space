import telegram
import os
from dotenv import load_dotenv
import random
import time
import argparse


def args_input(path):
    list_files = [os.path.join(address, name).replace('\\', '/')
                  for address, dirs, files in os.walk(path) for name in files]
    return list_files


def main():
    load_dotenv()
    bot = telegram.Bot(os.environ['BOT_TOKEN'])
    chat_id = bot.get_updates()[-1].message.chat_id
    list_images = args_input(path)
    default_period = 14400
    user_period = os.environ['USER_PERIOD']
    if user_period == '':
        period = default_period
    else:
        print(user_period)
        period = int(user_period) * 3600
    if len(list_images) > 0:
        while True:
            for file_path in list_images:
                bot.send_document(chat_id=chat_id, document = open(file_path, 'rb'))
                time.sleep(period)
            random.shuffle(list_images)
    else:
        print('Папка с фотографиями пуста или не существует')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Скрипт для автоматической публикации фотографий в Telegram'
    )
    parser.add_argument('path', type=str, help='launch id')
    args = parser.parse_args()
    path = args.path
    try:
        main()
    except telegram.error.NetworkError:
        print('Программа завершена')