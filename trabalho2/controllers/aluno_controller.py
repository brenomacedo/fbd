import sys
sys.path.append("..")

from utils.datetime_utils import getDate
from utils.erro_utils import printErro
from models.aluno import Aluno
from repositories.aluno_repository import AlunoRepository

class AlunosController:
    def __init__(self):
        self.alunoRepository = AlunoRepository()

    def createAluno(self):
        try:
            matricula = int(input('Matricula: '))
            nome = input('Nome: ')
            email = input('Email: ')
            nascimento = getDate('Nascimento (dd/mm/yyyy): ')
            endereco = input('Endereço: ')
            sexo = input('sexo ("masculino", "feminino", "nao-binario", "outro"): ')
            cursoId = input('cursoId: ')

            novoAluno = Aluno((matricula, nome, email, nascimento, endereco, sexo, cursoId))
            self.alunoRepository.create(novoAluno)
            print('Aluno inserido!')
        except Exception as erro:
            printErro(erro)

    def readAluno(self):
        try:
            alunos = self.alunoRepository.index()
            for aluno in alunos:
                print(aluno)
        except Exception as erro:
            printErro(erro)

    def updateAluno(self):
        try:
            matricula = int(input('Matricula: '))
            nome = input('Nome: ')
            email = input('Email: ')
            nascimento = getDate('Nascimento (dd/mm/yyyy): ')
            endereco = input('Endereço: ')
            sexo = input('sexo ("masculino", "feminino", "nao-binario", "outro"): ')
            cursoId = input('cursoId: ')

            alunoUpdate = Aluno((matricula, nome, email, nascimento, endereco, sexo, cursoId))
            self.alunoRepository.update(alunoUpdate)
            print('Aluno atualizado!')
        except Exception as erro:
            printErro(erro)

    def deleteAluno(self):
        try:
            matricula = int(input('matricula do aluno: '))
            self.alunoRepository.delete(matricula)
            print('Aluno deletado!')
        except Exception as erro:
            print(erro)