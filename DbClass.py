import sqlite3

class Database:

    def __init__(self, path: str) -> None:
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def execute(self, code) -> None:
        self.cursor.execute(code)

        self.conn.commit()

    def execute_args(self, code, args) -> None:
        self.cursor.execute(code, args)

        self.conn.commit()

    def select_all(self, code) -> list:
        self.cursor.execute(code)

        return self.cursor.fetchall()

    def select_all_args(self, code, args) -> list:
        self.cursor.execute(code, args)

        return self.cursor.fetchall()

    def select_one(self, code):
        self.cursor.execute(code)

        return self.cursor.fetchone()

    def select_one_args(self, code, args):
        self.cursor.execute(code, args)

        return self.cursor.fetchone()
