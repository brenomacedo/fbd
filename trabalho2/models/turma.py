class Turma:
    codigo: int
    periodo: str
    estado: str
    disciplinaId: int
    localId: int
    alunosMatriculados: int
    capacidade: int

    @staticmethod
    def fromArray(array):
        turmas = []
        for turma in array:
            novaTurma = Turma(turma)
            turmas.append(novaTurma)
        return turmas

    def __init__(self, tuple=None):
        self.codigo = tuple[0]
        self.periodo = tuple[1]
        self.estado = tuple[2]
        self.disciplinaId = tuple[3]
        self.localId = tuple[4]
        self.alunosMatriculados = tuple[5]
        self.capacidade = tuple[6]

    def __str__(self):
        return (
            f'==-==-==-==-== Codigo: {self.codigo} ==-==-==-==-==-==-==\n'
            f'Periodo: {self.periodo}; Estado: {self.estado}; disciplinaId: {self.disciplinaId}\n'
            f'localId: {self.localId}; alunosMatriculados: {self.alunosMatriculados}; capacidade: {self.capacidade}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )