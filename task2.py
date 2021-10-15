"""
2) створити скрипт який буде генерувати pdf документ з картинкою графіку
середньої загруженості процесора  за останні 10 періодів
(один період 2 години), тобто якщо в базу записуються дані що хвилини,
треба підрахувати середнє за 2 години, і такких 10 періодів,а далі на
основі 10 значень побудувати графік (дані беруться з бази 1 завдання)
"""

from exampledb import TableData
from typing import Tuple, Dict
from matplotlib import pyplot as plt
from fpdf import FPDF


db_object = TableData(database_name='example.sqlite', table_name='statistics')
part = len(db_object) // 10
main_dict_of_10periods = {}
dict_for_internal_period = {}


def main(data1: Dict[int, float], data2: Dict[int, float], db):
    counter = 0
    counter2 = 0
    for row in db:
        item = row[0:12]
        if counter < part:
            data1[counter] = avarage_for_row(item)
            counter += 1
        else:
            counter = 0
            avarage_for_period = avarage_for_group(data1)
            data2[counter2] = avarage_for_period
            counter2 += 1
    create_image(data2)
    create_pdf("diagram_task2.png")


def avarage_for_row(data: Tuple[float]) -> float:
    """:return: avarage value: float
    """
    summary = sum(data)
    return summary // len(data)


def avarage_for_group(data: Dict[int, int]) -> float:
    """And probably the same for group of rows
    :return: avarage value for group: float
    """
    values = data.values()
    summary = sum(values)
    return summary // len(data)


def create_image(data: Dict):
    cpu_hostory = list(map(lambda x: int(x), data.values()))
    plt.plot(cpu_hostory)
    plt.xlabel("Hours")
    plt.ylabel("CPU History")
    plt.savefig("diagram_task2.png")


def create_pdf(image_path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=10, w=90)
    pdf.set_font("Arial", size=12)
    pdf.ln(80)
    pdf.cell(200, 10, txt="{}".format(image_path), ln=1)
    pdf.output("diagram_task2.pdf")


if __name__ == "__main__":
    main(dict_for_internal_period, main_dict_of_10periods, db_object)
