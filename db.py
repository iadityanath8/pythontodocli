import sqlite3
from cli import Color
# connecting the sql-database

class Todo_DB:
    def __init__(self,db_name) -> None:
        self.DB_NAME = db_name
        self.CONN_COMMAND = '''  CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0
    )'''
        self.conn = None

        self.create_connection()
    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.DB_NAME)
            return self.conn
        except sqlite3.Error as e:
            print(e)
        return self.conn

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            # executing first command for creating the database
            cursor.execute(self.CONN_COMMAND)
            self.conn.commit()
            # print("Todo idem added successfully")
        except sqlite3.Error as e:
            print(e)
        
    
    def id_exist(self,id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(F"SELECT COUNT(*) FROM todos WHERE id = {id}")
            count = cursor.fetchone()[0]
            return count > 0
        except sqlite3.Error as e:
            print(Color.RED + e + Color.RESET)
            return False

    def add_todo(self,task):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"INSERT INTO todos (task) VALUES ('{task}')")
            self.conn.commit()
            print(Color.GREEN + "Todo added Successfully" + Color.RESET)
        except sqlite3.Error as e:
            print(Color.RED + e + Color.RED)

    def get_todos(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM todos")
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(Color.RED + e + Color.RED)

    def completed(self,id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"UPDATE todos SET completed = 1 WHERE id = {id}")
            self.conn.commit()
            print(Color.GREEN + "TODO marked completed" + Color.RESET)
        except sqlite3.Error as e:
            print(Color.RED + e + Color.RED)

    def delete_todo(self,id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"DELETE FROM todos WHERE id = {id}")
            self.conn.commit()
            print(Color.GREEN + "TODO DELETED SUCCESSFULLY" + Color.RESET)
        except sqlite3.Error as e:
            print(Color.RED + e + Color.RED)