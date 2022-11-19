import sys
sys.path.append("..")

from models.relacao_professores_disciplinas import RelacaoProfessoresDisciplinas
from .repository import Repository

class RelacaoProfessoresDisciplinasRepository(Repository):
    def create(self, relacao: RelacaoProfessoresDisciplinas):
        SQL = "INSERT INTO relacao_professores_disciplinas (professorId, disciplinaId) VALUES (%s, %s)"
        data = (relacao.professorId, relacao.disciplinaId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT id, professorId, disciplinaId FROM relacao_professores_disciplinas"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        relacoes = RelacaoProfessoresDisciplinas.fromArray(resultado)
        return relacoes

    def delete(self, id: int):
        SQL = "DELETE FROM relacao_professores_disciplinas WHERE id = %s"
        data = (id,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, relacao: RelacaoProfessoresDisciplinas):
        SQL = "UPDATE relacao_professores_disciplinas SET professorId = %s, disciplinaId = %s WHERE id = %s"
        data = (relacao.professorId, relacao.disciplinaId, relacao.id)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
