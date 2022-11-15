import sys
sys.path.append("..")

from database.database import databaseConnection
from models.avaliacao import Avaliacao
from .repository import Repository

class AvaliacaoRepository(Repository):
    def create(self, avaliacao: Avaliacao):
        SQL = "INSERT INTO avaliacoes (nota, tipo, alunosTurmasId) VALUES (%s, %s, %s)"
        data = (avaliacao.nota, avaliacao.tipo, avaliacao.alunosTurmasId)
        self.cursor.execute(SQL, data)
        self.connection.commit()

    def index(self):
        SQL = "SELECT id, nota, tipo, alunosTurmasId FROM avaliacoes"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        avaliacoes = Avaliacao.fromArray(resultado)
        return avaliacoes

    def delete(self, id: int):
        SQL = "DELETE FROM avaliacoes WHERE id = %s"
        data = (id,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, avaliacao: Avaliacao):
        SQL = "UPDATE avaliacoes SET id = %s, nota = %s, tipo = %s, alunosTurmasId = %s"
        data = (avaliacao.id, avaliacao.nota, avaliacao.tipo, avaliacao.alunosTurmasId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None