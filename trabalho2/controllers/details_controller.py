import sys
sys.path.append("..")

from models.aluno import Aluno
from models.avaliacao import Avaliacao
from models.turma import Turma
from models.local import Local
from models.disciplina import Disciplina
from models.dias_semana import DiasSemana
from models.relacao_turmas_dias_semana import RelacaoTurmasDiasSemana
from utils.erro_utils import printErro
from repositories.details_repository import DetailsRepository

class DetailsController:
    def __init__(self):
        self.detailsRepository = DetailsRepository()

    def consultarMediasDaTurma(self):
        try:
            turmaId = int(input('turmaId: '))
            medias = self.detailsRepository.indexMediaDosAlunosDeUmaTurma(turmaId)
            for media in medias:
                print(
                    f'==-==-==-==-== Matricula: {media[0].matricula} ==-==-==-==-==-==-==\n'
                    f'Nome: {media[0].nome}; Media: {media[1].nota}\n'
                    '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
                )
        except Exception as erro:
            printErro(erro)

    def consultarTurmasDeUmSemestre(self):
        try:
            semestre = input('semestre (XXXX.X - ex: 2022.1): ')
            turmas = self.detailsRepository.indexTurmasDeUmSemestre(semestre)
            for turma in turmas:
                print(turma)
        except Exception as erro:
            printErro(erro)

    def consultarLocaisEmUmBloco(self):
        try:
            bloco = int(input('bloco: '))
            locais = self.detailsRepository.locaisEmUmBloco(bloco)
            for local in locais:
                print(local)
        except Exception as erro:
            printErro(erro)

    def consultarTurmasEmUmLocal(self):
        try:
            localId = int(input('localId: '))
            turmas = self.detailsRepository.turmasEmUmLocal(localId)
            for turma in turmas:
                turmaAtual = turma[0]
                disciplinaAtual = turma[1]
                diasEHorarios = turma[2]
                print(f'==-==-==-==-== Matricula: {turmaAtual.codigo} ==-==-==-==-==-==-==')
                print(f'Nome da disciplina: {disciplinaAtual.nome}')
                for diaEHorario in diasEHorarios:
                    dia = diaEHorario[0]
                    horario = diaEHorario[1]
                    print(f'Dia: {dia.dia}; HorarioDeInicio: {horario.horarioDeInicio}; HoraioDeTermino: {horario.horarioDeTermino}')
                print('=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==')
        except Exception as erro:
            printErro(erro)

    def consultarHistoricoEscolar(self):
        try:
            matricula = int(input('matricula: '))
            medias = self.detailsRepository.historicoEscolar(matricula)
            for media in medias:
                print(
                    f'==-==-==-==-== Codigo da turma: {media[0].codigo} ==-==-==-==-==-==-==\n'
                    f'Media: {media[1].nota}\n'
                    '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
                )
        except Exception as erro:
            printErro(erro)