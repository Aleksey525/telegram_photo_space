import telegram
import os
from dotenv import load_dotenv
import random
import time
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Скрипт для автоматической публикации фотографий в Telegram'
    )
    parser.add_argument('path', type=str, help='launch id')
    args = parser.parse_args()
    path = args.path
    load_dotenv()
    bot = telegram.Bot(os.environ['BOT_TOKEN'])
    chat_id = bot.get_updates()[-1].message.chat_id
    names_files = [os.path.join(address, name).replace('\\', '/')
                   for address, dirs, files in os.walk(path) for name in files]
    default_period = 14400
    user_period = os.environ['USER_PERIOD']
    if not user_period:
        period = default_period
    else:
        period = int(user_period) * 3600
    try:
        while True:
            for file_path in names_files:
                if not file_path:
                    print('Папка с фотографиями пуста или не существует')
                    break
                with open(file_path, 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(period)
            random.shuffle(names_files)
    except telegram.error.NetworkError:
        print('Программа завершена')


if __name__ == '__main__':
    main()