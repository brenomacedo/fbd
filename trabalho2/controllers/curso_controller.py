import sys
sys.path.append("..")

from repositories.curso_repository import CursoRepository
from models.curso import Curso
from utils.erro_utils import printErro

class CursoController:
    def __init__(self):
        self.cursoRepository = CursoRepository()

    def createCurso(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            cargaHoraria = int(input('cargaHoraria: '))
            coordenadorId = int(input('coordenadorId: '))
            centroId = int(input('centroId: '))

            novoCurso = Curso((codigo, nome, cargaHoraria, coordenadorId, centroId))
            self.cursoRepository.create(novoCurso)
            print('Curso inserido!')
        except Exception as erro:
            printErro(erro)

    def readCurso(self):
        try:
            cursos = self.cursoRepository.index()
            for curso in cursos:
                print(curso)
        except Exception as erro:
            printErro(erro)
    
    def updateCurso(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            cargaHoraria = int(input('cargaHoraria: '))
            coordenadorId = int(input('coordenadorId: '))
            centroId = int(input('centroId: '))

            novoCurso = Curso((codigo, nome, cargaHoraria, coordenadorId, centroId))
            self.cursoRepository.update(novoCurso)
            print('Curso atualizado!')
        except Exception as erro:
            printErro(erro)

    def deleteCurso(self):
        try:
            codigo = int(input('codigo: '))
            self.cursoRepository.delete(codigo)
        except Exception as erro:
            printErro(erro)