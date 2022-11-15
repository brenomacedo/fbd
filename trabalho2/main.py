from database.database import databaseConnection
from models.disciplina import Disciplina
from repositories.disciplinarepository import DisciplinaRespository
from datetime import date

def main():
    disciplinas = DisciplinaRespository().delete(777)

if __name__ == '__main__':
    main()