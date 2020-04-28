import sqlite3

class Database:
    def __init__(self,db):
        self.db = db
        sqliteConnection = sqlite3.connect(self.db)
        self.cursor = sqliteConnection.cursor()

    # def execute_all(self, command):
    #     self.cursor.execute(command)
    #     records = self.cursor.fetchall()
    #     self.cursor.close()
    #     return records

    def fetch_one(self, command, *s):
        self.cursor.execute(command, s)
        records = self.cursor.fetchone()
        self.cursor.close()
        return records

    def fetch_all(self, command, *s):
        self.cursor.execute(command, s)
        records = self.cursor.fetchall()
        self.cursor.close()
        return records
