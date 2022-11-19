import sys
sys.path.append("..")

from models.relacao_professores_disciplinas import RelacaoProfessoresDisciplinas
from repositories.relacao_professores_disciplinas_repository import RelacaoProfessoresDisciplinasRepository
from utils.erro_utils import printErro

class RelacaoProfessoresDisciplinasController:
    def __init__(self):
        self.relacao_professores_disciplinas_repository = RelacaoProfessoresDisciplinasRepository()
    
    def createRelacaoProfessoresDisciplinas(self):
        try:
            professorId = int(input('professorId: '))
            disciplinaId = int(input('disciplinaId: '))

            novaRelacao = RelacaoProfessoresDisciplinas((None, professorId, disciplinaId))
            self.relacao_professores_disciplinas_repository.create(novaRelacao)
            print('Relacao inserida!')
        except Exception as erro:
            printErro(erro)

    def readRelacaoProfessoresDisciplinas(self):
        try:
            relacoes = self.relacao_professores_disciplinas_repository.index()
            for relacao in relacoes:
                print(relacao)
        except Exception as erro:
            printErro(erro)

    def updateRelacaoProfessoresDisciplinas(self):
        try:
            id = int(input('id: '))
            professorId = int(input('professorId: '))
            disciplinaId = int(input('disciplinaId: '))

            novaRelacao = RelacaoProfessoresDisciplinas((id, professorId, disciplinaId))
            self.relacao_professores_disciplinas_repository.update(novaRelacao)
            print('Relacao atualizada!')
        except Exception as erro:
            printErro(erro)

    def deleteRelacaoProfessoresDisciplinas(self):
        try:
            id = int(input('id: '))
            
            self.relacao_professores_disciplinas_repository.delete(id)
            print('Relacao deletada!')
        except Exception as erro:
            printErro(erro)