import sys
sys.path.append("..")

from models.professor import Professor
from .repository import Repository

class ProfessorRepository(Repository):
    def create(self, professor: Professor):
        SQL = "INSERT INTO professores (codigo, nome, email, sexo, formacao, nascimento) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (professor.codigo, professor.nome, professor.email, professor.sexo, professor.formacao, professor.nascimento)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT codigo, nome, email, sexo, formacao, nascimento FROM professores"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        professores = Professor.fromArray(resultado)
        return professores

    def delete(self, codigo: int):
        SQL = "DELETE FROM professores WHERE codigo = %s"
        data = (codigo,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
    
    def update(self, professor: Professor):
        SQL = "UPDATE professores SET nome = %s, email = %s, sexo = %s, formacao = %s, nascimento = %s WHERE codigo = %s"
        data = (professor.nome, professor.email, professor.sexo, professor.formacao, professor.nascimento, professor.codigo)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None