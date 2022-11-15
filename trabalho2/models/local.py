class Local:
    codigo: int
    nome: str
    bloco: int
    lotacao: int
    descricao: str
    tipo: str
    centroId: int

    @staticmethod
    def fromArray(array):
        locais = []
        for local in array:
            novoLocal = Local(local)
            locais.append(novoLocal)
        return locais

    def __init__(self, tuple=None):
        if tuple:
            self.codigo = tuple[0]
            self.nome = tuple[1]
            self.bloco = tuple[2]
            self.lotacao = tuple[3]
            self.descricao = tuple[4]
            self.tipo = tuple[5]
            self.centroId = tuple[6]

    def __str__(self):
        return (
            f'==-==-==-==-== Codigo: {self.codigo} ==-==-==-==-==-==-==\n'
            f'Nome: {self.nome}; bloco: {self.bloco}; lotacao: {self.lotacao}\n'
            f'descricao: {self.descricao}; tipo: {self.tipo}; centroId: {self.centroId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )