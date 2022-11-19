import sys
sys.path.append("..")

from repositories.relacao_cursos_disciplinas_repository import RelacaoCursosDisciplinasRepository
from utils.erro_utils import printErro
from models.relacao_cursos_disciplinas import RelacaoCursosDisciplinas

class RelacaoCursosDisciplinasController:
    def __init__(self):
        self.relacao_cursos_disciplinas_repository = RelacaoCursosDisciplinasRepository()

    def createRelacaoCursosDisciplinas(self):
        try:
            cursoId = int(input('cursoId: '))
            disciplinaId = int(input('disciplinaId: '))

            novaRelacao = RelacaoCursosDisciplinas((None, cursoId, disciplinaId))
            self.relacao_cursos_disciplinas_repository.create(novaRelacao)
            print('Relacao inserida!')
        except Exception as erro:
            printErro(erro)

    def readRelacaoCursosDisciplinas(self):
        try:
            relacoes = self.relacao_cursos_disciplinas_repository.index()
            for relacao in relacoes:
                print(relacao)
        except Exception as erro:
            printErro(erro)

    def updateRelacaoCursosDisciplinas(self):
        try:
            id = int(input('id: '))
            cursoId = int(input('cursoId: '))
            disciplinaId = int(input('disciplinaId: '))

            novaRelacao = RelacaoCursosDisciplinas((id, cursoId, disciplinaId))
            self.relacao_cursos_disciplinas_repository.update(novaRelacao)
            print('Relacao atualizada!')
        except Exception as erro:
            printErro(erro)

    def deleteRelacaoCursosDisciplinas(self):
        try:
            id = int(input('id: '))
            
            self.relacao_cursos_disciplinas_repository.delete(id)
            print('Relacao deletada!')
        except Exception as erro:
            printErro(erro)