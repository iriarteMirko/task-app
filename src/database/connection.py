import sqlite3 as sql

class ConnectionDatabase:
    def __init__(self):
        self.conn = sql.connect('src/database/db.sqlite3')
        self.cursor = self.conn.cursor()
    
    def __enter__(self):
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()