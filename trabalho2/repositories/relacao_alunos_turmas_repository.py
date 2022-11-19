import sys
sys.path.append("..")

from models.relacao_alunos_turmas import RelacaoAlunosTurmas
from .repository import Repository

class RelacaoAlunosTurmasRepository(Repository):
    def create(self, relacao: RelacaoAlunosTurmas):
        SQL = "INSERT INTO relacao_alunos_turmas (alunoId, turmaId) VALUES (%s, %s)"
        data = (relacao.alunoId, relacao.turmaId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT id, alunoId, turmaId FROM relacao_alunos_turmas"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        relacoes = RelacaoAlunosTurmas.fromArray(resultado)
        return relacoes

    def delete(self, id: int):
        SQL = "DELETE FROM relacao_alunos_turmas WHERE id = %s"
        data = (id,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, relacao: RelacaoAlunosTurmas):
        SQL = "UPDATE relacao_alunos_turmas SET alunoId = %s, turmaId = %s WHERE id = %s"
        data = (relacao.alunoId, relacao.turmaId, relacao.id)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
