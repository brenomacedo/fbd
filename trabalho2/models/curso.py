class Curso:
    codigo: int
    nome: str
    cargaHoraria: int
    coordenadorId: int
    centroId: int

    @staticmethod
    def fromArray(array):
        cursos = []
        for curso in array:
            novoCurso = Curso(curso)
            cursos.append(novoCurso)
        return cursos

    def __init__(self, tuple=None):
        if tuple:
            self.codigo = tuple[0]
            self.nome = tuple[1]
            self.cargaHoraria = tuple[2]
            self.coordenadorId = tuple[3]
            self.centroId = tuple[4]

    def __str__(self):
        return (
            f'==-==-==-==-== Codigo: {self.codigo} ==-==-==-==-==-==-==\n'
            f'Nome: {self.nome}; cargaHoraria: {self.cargaHoraria};\n'
            f'coordenadorId: {self.coordenadorId}; centroId: {self.centroId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )