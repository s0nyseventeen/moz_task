"""
1) Написати телеграм бота на основі HTTP BOT API  використовуючи бібліотеку requests
який буде кожні N хв присилати повідомлення  про стан загруженості кожного ядра процесора (в відсотках) а також інформацію про загруженість оперативної памяті
для отримання інформації про стан ресурсів можна скористатись бібліотекою psutil
також бот повинет записувати отримані заміри в базу даних
* для візуалізації можна за допомогою Mathplotlib згенерувати графік/діагарамку загруженості ресурсів  та надсилати повідомлення з картинкою
"""

import requests as r
import psutil
from time import sleep
from random import randint


def main(N: int):
    while True:
        sleep(N)
        send_message(randint(0, 9))


def send_message(data: str):
    API_LINK = "https://api.telegram.org/bot"
    TOKEN = "2081315834:AAHFuHw9VSsgj-VWKnc9aVT5GewWt4bgeBY"
    chat_id = "658316569"
    url = f"{API_LINK}{TOKEN}/sendMessage?chat_id={chat_id}&text={data}"
    results = r.get(url)
    return results.json()


    

def get_cpu_ram():
    pass




if __name__ == "__main__":
    main(5)

#updates_from_human = r.get("".join([API_LINK, TOKEN, "/getUpdates"])).json()
#
#print(updates_from_human)

#message_from_bot = updates_from_human["result"][0]["message"]
#chat_id = message_from_bot["from"]["id"]
#text = message_from_bot["text"]
#sent_message = r.get(f"{API_LINK}/sendMessage?chat_id={chat_id}&text=hi, you wrote {text}")


