import sys
sys.path.append("..")

from repositories.professor_repository import ProfessorRepository
from models.professor import Professor
from utils.erro_utils import printErro
from utils.datetime_utils import getDate

class ProfessorController:
    def __init__(self):
        self.professorRepository = ProfessorRepository()

    def createProfessor(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            email = input('email: ')
            sexo = input('sexo ("masculino", "feminino", "nao-binario", "outro"): ')
            formacao = input('formacao ("mestrado", "doutorado"): ')
            nascimento = getDate('nascimento (dd/mm/yyyy): ')

            novoProfessor = Professor((codigo, nome, email, sexo, formacao, nascimento))
            self.professorRepository.create(novoProfessor)
            print('Professor criado!')
        except Exception as erro:
            printErro(erro)

    def readProfessor(self):
        try:
            professores = self.professorRepository.index()
            for professor in professores:
                print(professor)
        except Exception as erro:
            printErro(erro)

    def updateProfessor(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            email = input('email: ')
            sexo = input('sexo ("masculino", "feminino", "nao-binario", "outro"): ')
            formacao = input('formacao ("mestrado", "doutorado"): ')
            nascimento = getDate('nascimento (dd/mm/yyyy): ')

            novoProfessor = Professor((codigo, nome, email, sexo, formacao, nascimento))
            self.professorRepository.update(novoProfessor)
            print('Professor atualizado!')
        except Exception as erro:
            printErro(erro)

    def deleteProfessor(self):
        try:
            codigo = int(input('codigo: '))
            self.professorRepository.delete(codigo)
            print('Professor deletado!')
        except Exception as erro:
            printErro(erro)
