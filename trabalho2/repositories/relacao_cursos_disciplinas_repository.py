import sys
sys.path.append("..")

from models.relacao_cursos_disciplinas import RelacaoCursosDisciplinas
from .repository import Repository

class RelacaoCursosDisciplinasRepository(Repository):
    def create(self, relacao: RelacaoCursosDisciplinas):
        SQL = "INSERT INTO relacao_cursos_disciplinas (cursoId, disciplinaId) VALUES (%s, %s)"
        data = (relacao.cursoId, relacao.disciplinaId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT id, cursoId, disciplinaId FROM relacao_cursos_disciplinas"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        relacoes = RelacaoCursosDisciplinas.fromArray(resultado)
        return relacoes

    def delete(self, id: int):
        SQL = "DELETE FROM relacao_cursos_disciplinas WHERE id = %s"
        data = (id,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, relacao: RelacaoCursosDisciplinas):
        SQL = "UPDATE relacao_cursos_disciplinas SET cursoId = %s, disciplinaId = %s WHERE id = %s"
        data = (relacao.cursoId, relacao.disciplinaId, relacao.id)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
