import requests
import time


API_URL: str ='https://api.telegram.org/bot'
BOT_TOKEN: str ='6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'
TEXT: str ='Хоп Хей лалаллей'
MAX_COUNTER: int = 100

offset: int =-2
counter: int = 0
chat_id: int


while counter < MAX_COUNTER:
    print('attemt = ', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id =result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
            time.sleep(1)
            counter +=1
