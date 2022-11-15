class Centro:
    codigo: int
    nome: str
    campusId: int
    diretorId: int

    @staticmethod
    def fromArray(array):
        centros = []
        for centro in array:
            novoCentro = Centro(centro)
            centros.append(novoCentro)
        return centros

    def __init__(self, tuple=None):
        if tuple:
            self.codigo = tuple[0]
            self.nome = tuple[1]
            self.campusId = tuple[2]
            self.diretorId = tuple[3]

    def __str__(self):
        return (
            f'==-==-==-==-== Codigo: {self.codigo} ==-==-==-==-==-==-==\n'
            f'Nome: {self.nome}; campusId: {self.campusId}; diretorId: {self.diretorId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )