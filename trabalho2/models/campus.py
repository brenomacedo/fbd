class Campus:
    codigo: int
    nome: str
    localizacao: str
    indicadoPor: int

    @staticmethod
    def fromArray(array):
        campi = []
        for campus in array:
            novoCampus = Campus(campus)
            campi.append(novoCampus)
        return campi


    def __init__(self, tuple=None):
        if tuple:
            self.codigo = tuple[0]
            self.nome = tuple[1]
            self.localizacao = tuple[2]
            self.indicadoPor = tuple[3]

    def __str__(self):
        return (
            f'==-==-==-==-== Codigo: {self.codigo} ==-==-==-==-==-==-==\n'
            f'Nome: {self.nome}; Localização: {self.localizacao}; indicadoPor: {self.indicadoPor}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )