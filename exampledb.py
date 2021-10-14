import sqlite3
from typing import List


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.database_name)
        self.cur = self.conn.cursor()

    def __iter__(self):
        yield from self.cur.execute(
            f"SELECT * FROM {self.table_name}"
        )

    def __len__(self):
        self.cur.execute(
            f"SELECT COUNT(*) FROM {self.table_name}"
        )
        return self.cur.fetchone()[0]  # !!! why return fetchone[0]

    def create_table(self):
        self.cur.execute(
            f"CREATE TABLE {self.table_name} "
            f"(core1 integer,"
            f"core2 integer,"
            f"core3 integer,"
            f"core4 integer,"
            f"core5 integer,"
            f"core6 integer,"
            f"core7 integer,"
            f"core8 integer,"
            f"core9 integer,"
            f"core10 integer,"
            f"core11 integer,"
            f"core12 integer,"
            f"ram integer)"
        )

    def insert(self, core_info: List[float], ram_info: float):
        core1, core2, core3, core4, core5, core6, core7, core8, core9, core10, \
            core11, core12 = core_info
        self.cur.execute(
            f"INSERT INTO {self.table_name} VALUES ("
            f"{core1},"
            f"{core2},"
            f"{core3},"
            f"{core4},"
            f"{core5},"
            f"{core6},"
            f"{core7},"
            f"{core8},"
            f"{core9},"
            f"{core10},"
            f"{core11},"
            f"{core12},"
            f"{ram_info})"
        )
        self.conn.commit()

    def get_info(self):
        with self.conn:
            self.cur.execute(
                f"SELECT * FROM {self.table_name}"
            )
            print(self.cur.fetchall())

    def close_connection(self):
        self.cur().close()
        self.conn.close()
