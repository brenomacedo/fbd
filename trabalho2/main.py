from database.database import databaseConnection
from models.turma import Turma
from repositories.turmarepository import TurmaRepository
from datetime import date

def main():
    professores = TurmaRepository().delete(555)
    # for professor in professores:
    #     print(professor)

if __name__ == '__main__':
    main()