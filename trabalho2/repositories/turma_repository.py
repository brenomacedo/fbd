import sys
sys.path.append("..")

from models.turma import Turma
from .repository import Repository

class TurmaRepository(Repository):
    def create(self, turma: Turma):
        SQL = "INSERT INTO turmas (codigo, periodo, estado, disciplinaId, localId, alunosMatriculados, capacidade) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (turma.codigo, turma.periodo, turma.estado, turma.disciplinaId, turma.localId, turma.alunosMatriculados, turma.capacidade)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT codigo, periodo, estado, disciplinaId, localId, alunosMatriculados, capacidade FROM turmas"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        turmas = Turma.fromArray(resultado)
        return turmas

    def delete(self, codigo: int):
        SQL = "DELETE FROM turmas WHERE codigo = %s"
        data = (codigo,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, turma: Turma):
        SQL = "UPDATE turmas SET periodo = %s, estado = %s, disciplinaId = %s, localId = %s, alunosMatriculados = %s, capacidade = %s WHERE codigo = %s"
        data = (turma.periodo, turma.estado, turma.disciplinaId, turma.localId, turma.alunosMatriculados, turma.capacidade, turma.codigo)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None                