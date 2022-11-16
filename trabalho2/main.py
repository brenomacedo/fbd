from database.database import databaseConnection
from models.professor import Professor
from repositories.professorrepository import ProfessorRepository
from datetime import date

def main():
    professores = ProfessorRepository().delete(11)
    # for professor in professores:
    #     print(professor)

if __name__ == '__main__':
    main()