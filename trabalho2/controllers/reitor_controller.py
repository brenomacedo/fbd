import sys
sys.path.append("..")

from models.reitor import Reitor
from repositories.reitor_repository import ReitorRepository
from utils.datetime_utils import getDate
from utils.erro_utils import printErro

class ReitorController:
    def __init__(self):
        self.reitorRepository = ReitorRepository()

    def createReitor(self):
        try:
            dataDeAdmissao = getDate('Data de admissao (dd/mm/yyyy):')
            professorId = int(input('professorId: '))

            novoReitor = Reitor((None, dataDeAdmissao, professorId))
            self.reitorRepository.create(novoReitor)
            print('Reitor criado!')
        except Exception as erro:
            printErro(erro)

    def readReitor(self):
        try:
            reitores = self.reitorRepository.index()
            for reitor in reitores:
                print(reitor)
        except Exception as erro:
            printErro(erro)

    def updateReitor(self):
        try:
            id = int(input('id: '))
            dataDeAdmissao = getDate('Data de admissao (dd/mm/yyyy):')
            professorId = int(input('professorId: '))

            novoReitor = Reitor((id, dataDeAdmissao, professorId))
            self.reitorRepository.update(novoReitor)
            print('Reitor atualizado!')
        except Exception as erro:
            printErro(erro)

    def deleteReitor(self):
        try:
            id = int(input('id: '))
            self.reitorRepository.delete(id)
            print('Reitor deletado!')
        except Exception as erro:
            printErro(erro)