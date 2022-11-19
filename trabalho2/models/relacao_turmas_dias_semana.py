from datetime import time

class RelacaoTurmasDiasSemana:
    id: int
    turmaId: int
    diaSemanaId: int
    horarioDeInicio: str
    horarioDeTermino: str

    @staticmethod
    def fromArray(array):
        relacoes = []
        for relacao in array:
            novaRelacao = RelacaoTurmasDiasSemana(relacao)
            relacoes.append(novaRelacao)
        return relacoes

    def __init__(self, tuple=None):
        time().str
        if tuple:
            self.id = tuple[0]
            self.turmaId = tuple[1]
            self.diaSemanaId = tuple[2]
            self.horarioDeInicio = tuple[3].strftime('%H:%M:%S')

    def __str__(self):
        return (
            f'==-==-==-==-== Id: {self.id} ==-==-==-==-==-==-==\n'
            f'turmaId: {self.turmaId}; diaSemanaId: {self.diaSemanaId}\n'
            f'horarioDeInicio: {self.horarioDeInicio}; horarioDeTermino: {self.horarioDeTermino}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )