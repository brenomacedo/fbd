import sys
sys.path.append("..")

from database.database import databaseConnection
from models.aluno import Aluno
from .repository import Repository

class AlunoRepository(Repository):
    def create(self, aluno: Aluno):
        SQL = "INSERT INTO alunos (matricula, nome, email, nascimento, endereco, sexo, cursoId) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (aluno.matricula, aluno.nome, aluno.email, aluno.nascimento, aluno.endereco, aluno.sexo, aluno.cursoId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
    
    def index(self):
        SQL = "SELECT matricula, nome, email, nascimento, endereco, sexo, cursoId FROM alunos"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        alunos = Aluno.fromArray(resultado)
        return alunos

    def delete(self, matricula: int):
        SQL = "DELETE FROM alunos WHERE matricula = %s"
        data = (matricula,)
        self.cursor.execute(
            SQL, data
        )
        self.connection.commit()
        return None

    def update(self, aluno: Aluno):
        SQL = "UPDATE alunos SET nome = %s, email = %s, nascimento = %s, endereco = %s, sexo = %s, cursoId = %s WHERE matricula = %s"
        data = (aluno.nome, aluno.email, aluno.nascimento, aluno.endereco, aluno.sexo, aluno.cursoId, aluno.matricula)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
