from datetime import date

class Aluno:
    matricula: int;
    nome: str;
    email: str;
    nascimento: str;
    endereco: str;
    sexo: str;
    cursoId: str;

    @staticmethod
    def fromArray(array):
        alunos = []
        for aluno in array:
            novoAluno = Aluno(aluno)
            alunos.append(novoAluno)
        return alunos

    def __init__(self, tuple=None):
        if tuple:
            self.matricula = tuple[0]
            self.nome = tuple[1]
            self.email = tuple[2]
            self.nascimento = tuple[3].strftime('%Y-%m-%d')
            self.endereco = tuple[4]
            self.sexo = tuple[5]
            self.cursoId = tuple[6]

    def __str__(self):
        return (
            f'==-==-==-==-== Matricula: {self.matricula} ==-==-==-==-==-==-==\n'
            f'Nome: {self.nome}; Email: {self.email}; Nascimento: {self.nascimento}\n'
            f'Endereço: {self.endereco}; Sexo: {self.sexo}; CursoId: {self.cursoId}\n'
            '=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n'
        )