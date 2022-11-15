from database.database import databaseConnection
# from models.aluno import Aluno
# from repositories.alunorepository import AlunoRepository
# from models.avaliacao import Avaliacao
# from repositories.avaliacaorepository import AvaliacaoRepository
from models.campus import Campus
from repositories.campusrepository import CampusRepository
from datetime import date

def main():
    campi = CampusRepository().delete(111)

if __name__ == '__main__':
    main()