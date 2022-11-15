from database.database import databaseConnection
from models.local import Local
from repositories.localrepository import LocalRepository
from datetime import date

def main():
    locais = LocalRepository().delete(888)

if __name__ == '__main__':
    main()