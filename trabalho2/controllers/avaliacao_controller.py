import sys
sys.path.append("..")

from repositories.avaliacao_repository import AvaliacaoRepository
from utils.erro_utils import printErro
from models.avaliacao import Avaliacao

class AvaliacaoController:
    def __init__(self):
        self.avaliacaoRepository = AvaliacaoRepository()

    def createAvaliacao(self):
        try:
            nota = float(input('Nota: '))
            tipo = input('Tipo: ("prova", "trabalho"): ')
            alunosTurmasId = int(input('alunosTurmasId: '))

            novaAvaliacao = Avaliacao((None, nota, tipo, alunosTurmasId))
            self.avaliacaoRepository.create(novaAvaliacao)
            print('Avaliacao inserida!')
        except Exception as erro:
            printErro(erro)

    def readAvaliacao(self):
        try:
            avaliacoes = self.avaliacaoRepository.index()
            for avaliacao in avaliacoes:
                print(avaliacao)
        except Exception as erro:
            printErro(erro)

    def updateAvaliacao(self):
        try:
            id = int(input('Id: '))
            nota = float(input('Nota: '))
            tipo = input('Tipo: ("prova", "avaliacao"): ')
            alunosTurmasId = int(input('alunosTurmasId: '))

            novaAvaliacao = Avaliacao((id, nota, tipo, alunosTurmasId))
            self.avaliacaoRepository.update(novaAvaliacao)
            print('Avaliacao atualizada!')
        except Exception as erro:
            printErro(erro)

    def deleteAvaliacao(self):
        try:
            id = int(input('Id: '))
            self.avaliacaoRepository.delete(id)
            print('Avaliacao deletada!')
        except Exception as erro:
            printErro(erro)