from database.database import databaseConnection
from models.curso import Curso
from repositories.cursorepository import CursoRepository
from datetime import date

def main():
    cursos = CursoRepository().delete(1111111)

if __name__ == '__main__':
    main()