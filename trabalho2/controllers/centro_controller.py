import sys
sys.path.append("..")

from repositories.centro_repository import CentroRepository
from utils.erro_utils import printErro
from models.centro import Centro

class CentroController:
    def __init__(self):
        self.centroRepository = CentroRepository()

    def createCentro(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            campusId = int(input('campusId: '))
            diretorId = int(input('diretorId: '))

            novoCentro = Centro((codigo, nome, campusId, diretorId))
            self.centroRepository.create(novoCentro)
            print('Campus criado!')
        except Exception as erro:
            printErro(erro)

    def readCentro(self):
        try:
            centros = self.centroRepository.index()
            for centro in centros:
                print(centro)
        except Exception as erro:
            printErro(erro)

    def updateCentro(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            campusId = int(input('campusId: '))
            diretorId = int(input('diretorId: '))

            novoCentro = Centro((codigo, nome, campusId, diretorId))
            self.centroRepository.update(novoCentro)
            print('Campus atualizado!')
        except Exception as erro:
            printErro(erro)

    def deleteCentro(self):
        try:
            codigo = int(input('codigo: '))
            self.centroRepository.delete(codigo)
            print('Campus deletado!')
        except Exception as erro:
            printErro(erro)
            