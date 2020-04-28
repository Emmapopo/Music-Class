import sqlite3

class Database:
    def __init__(self,db):
        self.db = db
        sqliteConnection = sqlite3.connect(self.db)
        self.cursor = sqliteConnection.cursor()

    def execute_all(self, command):
        self.cursor.execute(command)
        records = self.cursor.fetchall()
        self.cursor.close()
        return records

    def execute_id(self, command, id):
        self.cursor.execute(command, (id,))
        records = self.cursor.fetchone()
        self.cursor.close()
        return records

    def execute_search(self, command, s):
        x = '%' + s + '%'
        self.cursor.execute(command, (x,x))
        records = self.cursor.fetchall()
        self.cursor.close()
        return records
