import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'
offset: int = -2
updates: dict
timeout: int = 60

def do_somthing() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_somthing()


    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
