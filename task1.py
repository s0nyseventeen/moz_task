"""
1) Написати телеграм бота на основі HTTP BOT API  використовуючи бібліотеку requests
який буде кожні N хв присилати повідомлення  про стан загруженості кожного ядра процесора (в відсотках) а також інформацію про загруженість оперативної памяті
для отримання інформації про стан ресурсів можна скористатись бібліотекою psutil
також бот повинет записувати отримані заміри в базу даних
* для візуалізації можна за допомогою Mathplotlib згенерувати графік/діагарамку загруженості ресурсів  та надсилати повідомлення з картинкою
"""

import requests as r
import psutil

API_LINK = "https://api.telegram.org/bot2081315834:AAHFuHw9VSsgj-VWKnc9aVT5GewWt4bgeBY"
updates_from_human = r.get("".join([API_LINK, "/getUpdates"])).json()
message_from_bot = updates_from_human["result"][0]["message"]
chat_id = message_from_bot["from"]["id"]
text = message_from_bot["text"]
sent_message = r.get(f"{API_LINK}/sendMessage?chat_id={chat_id}&text=hi, you wrote {text}")
