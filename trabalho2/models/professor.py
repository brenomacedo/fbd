from datetime import date

class Professor:
    codigo: int
    nome: str
    email: str
    sexo: str
    formacao: str
    nascimento: str

    @staticmethod
    def fromArray(array):
        professores = []
        for professor in array:
            novoProfessor = Professor(professor)
            professores.append(novoProfessor)
        return professores

    def __init__(self, tuple=None):
        self.codigo = tuple[0]
        self.nome = tuple[1]
        self.email = tuple[2]
        self.sexo = tuple[3]
        self.formacao = tuple[4]
        self.nascimento = tuple[5].strftime('%Y-%m-%d')

    def __str__(self):
        return (
            f'==-==-==-==-== Codigo: {self.codigo} ==-==-==-==-==-==-==\n'
            f'Nome: {self.nome}; Email: {self.email}; Nascimento: {self.nascimento}\n'
            f'Formacao: {self.formacao}; Sexo: {self.sexo};\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )

