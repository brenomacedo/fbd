class RelacaoProfessoresDisciplinas:
    id: int
    professorId: int
    disciplinaId: int

    @staticmethod
    def fromArray(array):
        relacoes = []
        for relacao in array:
            novaRelacao = RelacaoProfessoresDisciplinas(relacao)
            relacoes.append(novaRelacao)
        return relacoes

    def __init__(self, tuple=None):
        if tuple:
            self.id = tuple[0]
            self.professorId = tuple[1]
            self.disciplinaId = tuple[2]

    def __str__(self):
        return (
            f'==-==-==-==-== Id: {self.id} ==-==-==-==-==-==-==\n'
            f'professorId: {self.professorId}; disciplinaId: {self.disciplinaId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )