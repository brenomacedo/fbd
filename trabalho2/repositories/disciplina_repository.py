import sys
sys.path.append("..")

from models.disciplina import Disciplina
from .repository import Repository

class DisciplinaRepository(Repository):
    def create(self, disciplina: Disciplina):
        SQL = "INSERT INTO disciplinas (codigo, nome, cargaHoraria, ementa) VALUES (%s, %s, %s, %s)"
        data = (disciplina.codigo, disciplina.nome, disciplina.cargaHoraria, disciplina.ementa)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT codigo, nome, cargaHoraria, ementa FROM disciplinas"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        disciplinas = Disciplina.fromArray(resultado)
        return disciplinas

    def delete(self, codigo: int):
        SQL = "DELETE FROM disciplinas WHERE codigo = %s"
        data = (codigo,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, disciplina: Disciplina):
        SQL = "UPDATE disciplinas SET nome = %s, cargaHoraria = %s, ementa = %s WHERE codigo = %s"
        data = (disciplina.nome, disciplina.cargaHoraria, disciplina.ementa, disciplina.codigo)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None