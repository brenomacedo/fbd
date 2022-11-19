import sys
sys.path.append("..")

from models.local import Local
from repositories.local_repository import LocalRepository
from utils.erro_utils import printErro

class LocalController:
    def __init__(self):
        self.localRepository = LocalRepository()

    def createLocal(self):
        codigo = int(input('codigo: '))
        nome = input('nome: ')
        bloco = int(input('bloco: '))
        lotacao = int(input('lotacao: '))
        descricao = input('descricao: ')
        tipo = input('tipo ("bloco", "sala_de_aula", "auditorio", "laboratorio"): ')
        centroId = int(input('centroId'))

        novoLocal = Local((codigo, nome, bloco, lotacao, descricao, tipo, centroId))
        self.localRepository.create(novoLocal)
        print('Local criado!')

    def readLocal(self):
        try:
            locais = self.localRepository.index()
            for local in locais:
                print(local)
        except Exception as erro:
            printErro(erro)
    
    def updateLocal(self):
        try:
            codigo = int(input('codigo: '))
            nome = input('nome: ')
            bloco = int(input('bloco: '))
            lotacao = int(input('lotacao: '))
            descricao = input('descricao: ')
            tipo = input('tipo ("bloco", "sala_de_aula", "auditorio", "laboratorio"): ')
            centroId = int(input('centroId'))

            novoLocal = Local((codigo, nome, bloco, lotacao, descricao, tipo, centroId))
            self.localRepository.update(novoLocal)
            print('Local atualizado!')
        except Exception as erro:
            printErro(erro)

    def deleteLocal(self):
        try:
            codigo = int(input('codigo: '))
            self.localRepository.delete(codigo)
            print('Local deletado!')
        except Exception as erro:
            printErro(erro)
