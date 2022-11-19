class RelacaoAlunosTurmas:
    id: int
    alunoId: int
    turmaId: int

    @staticmethod
    def fromArray(array):
        relacoes = []
        for relacao in array:
            novaRelacao = RelacaoAlunosTurmas(relacao)
            relacoes.append(novaRelacao)
        return relacoes

    def __init__(self, tuple=None):
        if tuple:
            self.id = tuple[0]
            self.alunoId = tuple[1]
            self.turmaId = tuple[2]

    def __str__(self):
        return (
            f'==-==-==-==-== Id: {self.id} ==-==-==-==-==-==-==\n'
            f'alunoId: {self.alunoId}; turmaId: {self.turmaId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )