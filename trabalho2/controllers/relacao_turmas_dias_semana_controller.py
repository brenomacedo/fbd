import sys
sys.path.append("..")

from models.relacao_turmas_dias_semana import RelacaoTurmasDiasSemana
from repositories.relacao_turmas_dias_semana_repository import RelacaoTurmasDiasSemanaRepository
from utils.erro_utils import printErro
from utils.datetime_utils import getTime

class RelacaoTurmasDiasSemanaController:
    def __init__(self):
        self.relacao_turmas_dias_semana_repository = RelacaoTurmasDiasSemanaRepository()

    def createRelacaoTurmasDiasSemana(self):
        try:
            turmaId = int(input('turmaId: '))
            diaSemanaId = int(input('diaSemanaId: '))
            horarioDeInicio = getTime('horarioDeInicio (HH:MM): ')
            horarioDeTermino = getTime('horarioDeTermino: (HH:MM): ')

            novaRelacao = RelacaoTurmasDiasSemana((None, turmaId, diaSemanaId, horarioDeInicio, horarioDeTermino))
            self.relacao_turmas_dias_semana_repository.create(novaRelacao)
            print('Relacao criada!')
        except Exception as erro:
            printErro(erro)

    def readRelacaoTurmasDiasSemana(self):
        try:
            relacoes = self.relacao_turmas_dias_semana_repository.index()
            for relacao in relacoes:
                print(relacao)
        except Exception as erro:
            printErro(erro)

    def updateRelacaoTurmasDiasSemana(self):
        try:
            id = int(input('id: '))
            turmaId = int(input('turmaId: '))
            diaSemanaId = int(input('diaSemanaId: '))
            horarioDeInicio = getTime('horarioDeInicio (HH:MM): ')
            horarioDeTermino = getTime('horarioDeTermino: (HH:MM): ')

            novaRelacao = RelacaoTurmasDiasSemana((id, turmaId, diaSemanaId, horarioDeInicio, horarioDeTermino))
            self.relacao_turmas_dias_semana_repository.update(novaRelacao)
            print('Relacao atualizada!')
        except Exception as erro:
            printErro(erro)

    def deleteRelacaoTurmasDiasSemana(self):
        try:
            id = int(input('id: '))

            self.relacao_turmas_dias_semana_repository.delete(id)
            print('Relacao deletada!')
        except Exception as erro:
            printErro(erro)