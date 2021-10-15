"""
1) Написати телеграм бота на основі HTTP BOT API  використовуючи
 бібліотеку requests
який буде кожні N хв присилати повідомлення  про стан загруженості
кожного ядра процесора (в відсотках) а також інформацію про загруженість
оперативної памяті
для отримання інформації про стан ресурсів можна скористатись бібліотекою
psutil також бот повинет записувати отримані заміри в базу даних
* для візуалізації можна за допомогою Mathplotlib згенерувати
графік/діагарамку загруженості ресурсів  та надсилати повідомлення з картинкою
"""

import requests as r
import psutil
from time import sleep
from typing import List
from exampledb import TableData
from matplotlib import pyplot as plt

db_object = TableData(database_name='example.sqlite', table_name='statistics')


def main(N_seconds: int):
    while True:
        core_data = get_core_usage()
        ram_data = get_ram_usage()
        db_object.insert(core_data, ram_data)
        show_image(core_data, ram_data)
        sleep(N_seconds)
        send_message()


def send_message():
    API_LINK = "https://api.telegram.org/bot"
    TOKEN = "2081315834:AAHFuHw9VSsgj-VWKnc9aVT5GewWt4bgeBY"
    chat_id = "658316569"
    files = {'photo': open('/home/stanislavk/Desktop/test_moz/mygraph.png', 'rb')}
    url = f"{API_LINK}{TOKEN}/sendPhoto?chat_id={chat_id}"
    results = r.post(url, files=files)
    return results.json()


def get_core_usage():
    data = psutil.cpu_freq(percpu=True)
    data_percentage = [round(x[0] / 100, 2) for x in data]
    return data_percentage


def get_ram_usage():
    return psutil.virtual_memory()[2]


def show_image(core_data: List[float], ram: float):
    x = ["1", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "11", "12", "RAM"]
    cores = list(map(lambda x: int(x), core_data))
    cores.append(int(ram))
    plt.bar(x, cores)
    plt.xlabel("cores")
    plt.ylabel("percentage %")
    plt.savefig("diagram_task1.png")


if __name__ == "__main__":
    main(5)
