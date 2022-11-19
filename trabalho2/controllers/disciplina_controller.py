import sys
sys.path.append("..")

from repositories.disciplina_repository import DisciplinaRepository
from utils.erro_utils import printErro
from models.disciplina import Disciplina

class DisciplinaController:
    def __init__(self):
        self.disciplinaRepository = DisciplinaRepository()

    def createDisciplina(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            cargaHoraria = int(input('cargaHoraria: '))
            ementa = input('ementa: ')

            novaDisciplina = Disciplina((codigo, nome, cargaHoraria, ementa))
            self.disciplinaRepository.create(novaDisciplina)
            print('Disciplina inserida!')
        except Exception as erro:
            printErro(erro)

    def readDisciplina(self):
        try:
            disciplinas = self.disciplinaRepository.index()
            for disciplina in disciplinas:
                print(disciplina)
        except Exception as erro:
            printErro(erro)

    def updateDisciplina(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            cargaHoraria = int(input('cargaHoraria: '))
            ementa = input('ementa: ')

            novaDisciplina = Disciplina((codigo, nome, cargaHoraria, ementa))
            self.disciplinaRepository.update(novaDisciplina)
            print('Disciplina atualizada!')
        except Exception as erro:
            printErro(erro)

    def deleteDisciplina(self):
        try:
            codigo = int(input('codigo: '))
            self.disciplinaRepository.delete(codigo)
            print('Disciplina deletada!')
        except Exception as erro:
            printErro(erro)