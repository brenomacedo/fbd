from database.database import databaseConnection
from models.reitor import Reitor
from repositories.reitorrepository import ReitorRepository
from datetime import date

def main():
    professores = ReitorRepository().delete(2)
    # for professor in professores:
    #     print(professor)

if __name__ == '__main__':
    main()