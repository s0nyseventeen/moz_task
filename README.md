1) Написати телеграм бота на основі HTTP BOT API  використовуючи бібліотеку 
requests який буде кожні N хв присилати повідомлення  про стан загруженості 
кожного ядра процесора (в відсотках) а також інформацію про загруженість 
оперативної памяті для отримання інформації про стан ресурсів можна 
скористатись бібліотекою psutil також бот повинет записувати отримані 
заміри в базу даних
* для візуалізації можна за допомогою Mathplotlib згенерувати графік/діагарамку
  загруженості ресурсів  та надсилати повідомлення з картинкою


2) створити скрипт який буде генерувати pdf документ з картинкою графіку 
середньої загруженості процесора  за останні 10 періодів
(один період 2 години), тобто якщо в базу записуються дані що хвилини, 
треба підрахувати середнє за 2 години, і такких 10 періодів,а далі на 
основі 10 значень побудувати графік (дані беруться з бази 1 завдання)


3) написати сервіс на Flask/Django який буде реалізовувати Rest API

- При POST запиті на endpoint /tags  з url веб сторінки в якості тіла 
сервіс повертає ідентифікатор задачі
- При GET запиті на  endpoint /tags/<ідентифікатор задачі> вертає 
підраховану кількість   html тегів які знаходяться на сторінці
приклад: {html: 1, head: 1, body: 1. p: 10, img: 2} або помилку якщо url 
вказує не на html cторінку
- При GET запиті на  endpoint /urls/ вертає перелік унікальних url які 
  були надані сервісу

* При GET запиті на endpoint /stats/ вертає json з даними які повинні містити :
  кількість унікальних url, кількість задач, сумарну кількість по кожному типу тега, 
  ід та дата виконання останньої задачі
* Оскільки завантаження і парсинг html сторінки може виконуватись тривалий час є сенс
  скористатись бібліотекою celery для асинхронного виконання парсигну
