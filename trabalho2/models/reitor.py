class Reitor:
    id: int
    dataDeAdmissao: str
    professorId: int

    @staticmethod
    def fromArray(array):
        reitores = []
        for reitor in array:
            novoReitor = Reitor(reitor)
            reitores.append(novoReitor)
        return reitores

    def __init__(self, tuple=None):
        if tuple:
            self.id = tuple[0]
            self.dataDeAdmissao = tuple[1].strftime('%Y-%m-%d')
            self.professorId = tuple[2]

    def __str__(self):
        return (
            f'==-==-==-==-== Id: {self.id} ==-==-==-==-==-==-==\n'
            f'dataDeAdmissao: {self.dataDeAdmissao}; professorId: {self.professorId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )