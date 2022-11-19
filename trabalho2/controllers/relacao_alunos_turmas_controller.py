import sys
sys.path.append("..")

from models.relacao_alunos_turmas import RelacaoAlunosTurmas
from repositories.relacao_alunos_turmas_repository import RelacaoAlunosTurmasRepository
from utils.erro_utils import printErro

class RelacaoAlunosTurmasController:
    def __init__(self):
        self.relacao_alunos_turmas_repository = RelacaoAlunosTurmasRepository()

    def createRelacaoAlunosTurmas(self):
        try:
            alunoId = int(input('alunoId: '))
            turmaId = int(input('turmaId: '))

            novaRelacao = RelacaoAlunosTurmas((None, alunoId, turmaId))
            self.relacao_alunos_turmas_repository.create(novaRelacao)
            print('Relacao inserida!')
        except Exception as erro:
            printErro(erro)

    def readRelacaoAlunosTurmas(self):
        try:
            relacoes = self.relacao_alunos_turmas_repository.index()
            for relacao in relacoes:
                print(relacoes)
        except Exception as erro:
            printErro(erro)

    def updateRelacaoAlunosTurmas(self):
        try:
            id = int(input('id: '))
            alunoId = int(input('alunoId: '))
            turmaId = int(input('turmaId: '))

            novaRelacao = RelacaoAlunosTurmas((id, alunoId, turmaId))
            self.relacao_alunos_turmas_repository.update(novaRelacao)
            print('Relacao atualizada!')
        except Exception as erro:
            printErro(erro)

    def deleteRelacaoAlunosTurmas(self):
        try:
            id = int(input('id: '))

            self.relacao_alunos_turmas_repository.delete(id)
            print('Relacao deletada!')
        except Exception as erro:
            printErro(erro)