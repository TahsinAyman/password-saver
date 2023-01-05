import sqlite3

# conn = sqlite3.connect('cust.db')

# c = conn.cursor()
# table = "photos"


class Fetch:
    def __init__(self, cursor: sqlite3.Cursor, table: str, row_id: bool) -> None:
        self.c = cursor
        self.t = table
        if row_id:
            self.command = f"SELECT rowid, * FROM {self.t}"
        else:
            self.command = f"SELECT * FROM {self.t}"

    def get_all(self) -> list:
        self.c.execute(self.command)
        return self.c.fetchall()


    def get_spec(self, component: str, string: str, starting: bool) -> list[tuple]:
        if starting:
            line = f" WHERE {component} LIKE '{string}%'"
        else:
            line = f" WHERE {component} LIKE '%{string}'"
        self.c.execute(self.command + line)

        return self.c.fetchall()

    def get_spec_commponent_str(self, component: str, string: str) -> list[tuple]:
        line = f" WHERE {component} = '{string}' "
        self.c.execute(self.command + line)
        return self.c.fetchall()

    def get_spec_commponent_str_many(self, condetion: str):
        line = " WHERE " + condetion
        print(self.command + line)

    def get_spec_commponent_int(self, component: str, operation: str, number: int) -> list[tuple]:
        line = f" WHERE {component} {operation} {number} "
        self.c.execute(self.command+line)
        return self.c.fetchall()

    def get_spec_rowid(self,id_number : int ) -> list[tuple] :
        self.c.execute(self.command + f" WHERE rowid = {id_number} ")
        return self.c.fetchall()


class Add:
    def __init__(self, cursor: sqlite3.Cursor, table: str) -> None:
        self.table = table
        self.c = cursor

    def insert_one(self, content: tuple | list) -> None:
        self.c.execute(f"INSERT INTO {self.table} VALUES (?,?,?)", content)

    def insert_many(self, content: list | tuple, ):
        values_count = len(content[0])
        x = ''.join(["?," for i in range(values_count)])
        x = x.removesuffix(",")
        x = f"({x})"
        self.c.executemany(f"INSERT INTO {self.table} VALUES " + x, content)


class Update:
    def __init__(self, cursor: sqlite3.Cursor, table: str) -> None:
        self.c = cursor
        self.command = f"UPDATE {table} SET "
        self.fetch_obj = Fetch(cursor, table=table, row_id=True)

    def update_records_str(self, component: str, string: str, condition: str) -> None:
        line = f"{component} = '{string}' WHERE {condition}"
        self.c.execute(self.command + line)

    def update_records_int(self, component: str, number: int, condition: str) -> None:
        line = f"{component} = {number} WHERE {condition}"
        self.c.execute(self.command + line)

    def update_rowid(self) -> None:
        all_qry = self.fetch_obj.get_all()
        qry_length = len(all_qry)
        for i in range(1, qry_length+1):
            self.update_records_int('rowid', i, f" rowid = {all_qry[i-1][0]}")



def delete(cursor: sqlite3.Cursor, table: str, condition: str) -> None:
    cursor.execute(f"DELETE FROM {table} WHERE {condition}")


def delete_table(cursor: sqlite3.Cursor, table:str) -> None:
    cursor.execute(F"DELETE {table}")



def create(cursor: sqlite3.Cursor, table: str, **kwargs: str) -> None:
    line = f'CREATE TABLE {table} '
    paran = "". join([i + ' ' + kwargs[i] + ', ' for i in kwargs])
    paran = paran.removesuffix(', ')
    paran = f"({paran})"
    cursor.execute(line + paran)


# create(c, table='photos', name="text", photos="blob")




