import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://aws.random.cat/meow'
BOT_TOKEN: str = '6089944231:AAG9SB-CeDIPozAAT7DCNzs7mxplaFOuqLg'
# TEXT: str ='Хоп Хей лалаллей'
# MAX_COUNTER: int = 100


offset: int =-2
counter: int = 0
cat_response: requests.Response
cat_link: str


# chat_id: int


while counter < 100:
    print('attemt = ', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter +=1








# while counter < MAX_COUNTER:
#     print('attemt = ', counter)

#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id =result['message']['from']['id']
#             requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
#             time.sleep(1)
#             counter +=1
