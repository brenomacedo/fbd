class Avaliacao:
    id: int
    nota: float
    tipo: str
    alunosTurmasId: int

    @staticmethod
    def fromArray(array):
        avaliacoes = []
        for avaliacao in array:
            novaAvaliacao = Avaliacao(avaliacao)
            avaliacoes.append(novaAvaliacao)
        return avaliacoes

    def __init__(self, tuple=None):
        if tuple:
            self.id = tuple[0]
            self.nota = tuple[1]
            self.tipo = tuple[2]
            self.alunosTurmasId = tuple[3]

    def __str__(self):
        return (
            f'==-==-==-==-== Id: {self.id} ==-==-==-==-==-==-==\n'
            f'Nota: {self.nota}; Tipo: {self.tipo}; alunosTurmasId: {self.alunosTurmasId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )