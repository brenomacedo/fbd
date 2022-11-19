import sys
sys.path.append("..")

from repositories.campus_repository import CampusRepository
from utils.erro_utils import printErro
from models.campus import Campus

class CampusController:
    def __init__(self):
        self.campusRepository = CampusRepository()

    def createCampus(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            localizacao = input('localizacao: ')
            indicadoPor = int(input('indicadoPor (id do reitor que indicou): '))

            novoCampus = Campus((codigo, nome, localizacao, indicadoPor))
            self.campusRepository.create(novoCampus)
            print('Campus inserido!')
        except Exception as erro:
            printErro(erro)

    def readCampus(self):
        try:
            campi = self.campusRepository.index()
            for campus in campi:
                print(campus)
        except Exception as erro:
            printErro(erro)

    def updateCampus(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            localizacao = input('localizacao: ')
            indicadoPor = int(input('indicadoPor (id do reitor que indicou): '))

            novoCampus = Campus((codigo, nome, localizacao, indicadoPor))
            self.campusRepository.update(novoCampus)
            print('Campus atualizado!')
        except Exception as erro:
            printErro(erro)

    def deleteCampus(self):
        try:
            codigo = int(input('codigo: '))
            self.campusRepository.delete(codigo)
            print('Campus deletado!')
        except Exception as erro:
            printErro(erro)