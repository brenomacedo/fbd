import sys
sys.path.append("..")

from repositories.turma_repository import TurmaRepository
from models.turma import Turma
from utils.erro_utils import printErro

class TurmaController:
    def __init__(self):
        self.turmaRepository = TurmaRepository()

    def createTurma(self):
        try:
            codigo = int(input('codigo: '))
            periodo = input('periodo (XXXX.X - ex: 2022.1): ')
            estado = input('estado ("aberta", "concluida"): ')
            disciplinaId = int(input('disciplinaId: '))
            localId = int(input('localId: '))
            alunosMatriculados = int(input('alunosMatriculados: '))
            capacidade = int(input('capacidade: '))

            novaTurma = Turma((codigo, periodo, estado, disciplinaId, localId, alunosMatriculados, capacidade))
            self.turmaRepository.create(novaTurma)
            print('Turma criada!')
        except Exception as erro:
            printErro(erro)

    def readTurma(self):
        try:
            turmas = self.turmaRepository.index()
            for turma in turmas:
                print(turma)
        except Exception as erro:
            printErro(erro)

    def updateTurma(self):
        try:
            codigo = int(input('codigo: '))
            periodo = input('periodo (XXXX.X - ex: 2022.1): ')
            estado = input('estado ("aberta", "concluida"): ')
            disciplinaId = int(input('disciplinaId: '))
            localId = int(input('localId: '))
            alunosMatriculados = int(input('alunosMatriculados: '))
            capacidade = int(input('capacidade: '))

            novaTurma = Turma((codigo, periodo, estado, disciplinaId, localId, alunosMatriculados, capacidade))
            self.turmaRepository.update(novaTurma)
            print('Turma atualizada!')
        except Exception as erro:
            printErro(erro)

    def deleteTurma(self):
        try:
            codigo = int(input('codigo: '))
            self.turmaRepository.delete(codigo)
            print('Turma deletada!')
        except Exception as erro:
            printErro(erro)