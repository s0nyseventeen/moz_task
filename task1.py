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
from typing import List
from exampledb import TableData

db_object = TableData(database_name='example.sqlite', table_name='statistics')


def main(N: int):
    while True:
        core_data = get_core_usage()
        ram_data = get_ram_usage()
        db_object.insert(core_data, ram_data)
        sleep(N)
        send_message(core_data, ram_data)


def send_message(core_data: List[float], ram_data: float):
    API_LINK = "https://api.telegram.org/bot"
    TOKEN = "2081315834:AAHFuHw9VSsgj-VWKnc9aVT5GewWt4bgeBY"
    chat_id = "658316569"
    url = f"{API_LINK}{TOKEN}/sendMessage?chat_id={chat_id}&text={core_data} " \
          f"RAM = {ram_data}%"
    results = r.get(url)
    return results.json()


def get_core_usage():
    data = psutil.cpu_freq(percpu=True)
    data_percentage = [round(x[0] / 100, 2) for x in data]
    return data_percentage


def get_ram_usage():
    return psutil.virtual_memory()[2]


if __name__ == "__main__":
    main(5)
