class RelacaoCursosDisciplinas:
    id: int
    cursoId: int
    disciplinaId: int

    @staticmethod
    def fromArray(array):
        relacoes = []
        for relacao in array:
            novaRelacao = RelacaoCursosDisciplinas(relacao)
            relacoes.append(novaRelacao)
        return relacoes

    def __init__(self, tuple=None):
        if tuple:
            self.id = tuple[0]
            self.cursoId = tuple[1]
            self.disciplinaId = tuple[2]

    def __str__(self):
        return (
            f'==-==-==-==-== Id: {self.id} ==-==-==-==-==-==-==\n'
            f'cursoId: {self.cursoId}; disciplinaId: {self.disciplinaId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )