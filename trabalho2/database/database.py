import json
import os

from psycopg2 import connect

config = None
configFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.config.json')

with open(configFilePath, 'r') as file:
    config = json.load(file)

class Connection:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __del__(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def initDb(self):
        self.conn = connect(host=config['host'], database=config['database'], user=config['user'], password=config['password'])
        self.cursor = self.conn.cursor()
    
    def getConnection(self):
        if not self.conn:
            try:
                self.initDb()
                return self.conn
            except:
                print('Erro ao iniciar a conexão.')
                return None
        return self.conn

    def getCursor(self):
        if not self.cursor:
            try:
                self.initDb()
                return self.cursor
            except:
                print('Erro ao iniciar a conexão.')
                return None
        return self.cursor

databaseConnection = Connection()