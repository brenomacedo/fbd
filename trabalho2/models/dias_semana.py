class DiasSemana:
    id: int
    dia: str

    @staticmethod
    def fromArray(array):
        diasSemana = []
        for diaSemana in array:
            novoDiaSemana = DiasSemana(diaSemana)
            diasSemana.append(novoDiaSemana)
        return diasSemana

    def __init__(self, tuple=None):
        if tuple:
            self.id = tuple[0]
            self.dia = tuple[1]

    def __str__(self):
        return (
            f'==-==-==-==-== Id: {self.id} ==-==-==-==-==-==-==\n'
            f'Dia: {self.dia};\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )