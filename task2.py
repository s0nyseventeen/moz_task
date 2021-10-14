"""
2) створити скрипт який буде генерувати pdf документ з картинкою графіку
середньої загруженості процесора  за останні 10 періодів
(один період 2 години), тобто якщо в базу записуються дані що хвилини,
треба підрахувати середнє за 2 години, і такких 10 періодів,а далі на
основі 10 значень побудувати графік (дані беруться з бази 1 завдання)
"""

from exampledb import TableData
from typing import Tuple, Dict

db_object = TableData(database_name='example.sqlite', table_name='statistics')
part = len(db_object) // 10  # 9


def avarage_for_row(data: Tuple[float]) -> float:
    """:return: avarage value: int
    """
    summary = sum(data)
    return summary // len(data)


def avarage_for_group(data: Dict) -> float:
    """And probably the same for group of rows
    :return: avarage value for group: int or float
    """
    values = data.values()
    summary = sum(values)
    return summary // len(data)


counter = 0
counter2 = 0
main_dict_of_10periods = {}
dict_for_internal_period = {}

for row in db_object:
    item = row[0:12]
    if counter <= part:
        dict_for_internal_period[counter] = avarage_for_row(item)
        counter += 1
    else:
        counter = 0
        avarage_for_period = avarage_for_group(dict_for_internal_period)
        main_dict_of_10periods[counter2] = avarage_for_period
        counter2 += 1

print(dict_for_internal_period)
print(main_dict_of_10periods)
