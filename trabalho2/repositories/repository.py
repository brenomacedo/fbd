import sys
sys.path.append("..")

from database.database import databaseConnection

class Repository:
    def __init__(self):
        self.connection = databaseConnection.getConnection()
        self.cursor = databaseConnection.getCursor()