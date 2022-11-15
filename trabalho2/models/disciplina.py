class Disciplina:
    codigo: int
    nome: str
    cargaHoraria: int
    ementa: str

    @staticmethod
    def fromArray(array):
        disciplinas = []
        for disciplina in array:
            novaDisciplina = Disciplina(disciplina)
            disciplinas.append(novaDisciplina)
        return disciplinas

    def __init__(self, tuple=None):
        self.codigo = tuple[0]
        self.nome = tuple[1]
        self.cargaHoraria = tuple[2]
        self.ementa = tuple[3]

    def __str__(self):
        return (
            f'==-==-==-==-== Codigo: {self.codigo} ==-==-==-==-==-==-==\n'
            f'Nome: {self.nome}; cargaHoraria: {self.cargaHoraria}; Ementa: {self.ementa}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )