import sys
sys.path.append("..")

from models.relacao_turmas_dias_semana import RelacaoTurmasDiasSemana
from .repository import Repository

class RelacaoTurmasDiasSemanaRepository(Repository):
    def create(self, relacao: RelacaoTurmasDiasSemana):
        SQL = "INSERT INTO relacao_turmas_diassemana (turmaId, diaSemanaId, horarioDeInicio, horarioDeTermino) VALUES (%s, %s, %s, %s)"
        data = (relacao.turmaId, relacao.diaSemanaId, relacao.horarioDeInicio, relacao.horarioDeTermino)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT id, turmaId, diaSemanaId, horarioDeInicio, horarioDeTermino FROM relacao_turmas_diassemana"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        relacoes = RelacaoTurmasDiasSemana.fromArray(resultado)
        return relacoes

    def delete(self, id: int):
        SQL = "DELETE FROM relacao_turmas_diassemana WHERE id = %s"
        data = (id,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, relacao: RelacaoTurmasDiasSemana):
        SQL = "UPDATE relacao_turmas_diassemana SET turmaId = %s, diaSemanaId = %s, horarioDeInicio = %s, horarioDeTermino = %s WHERE id = %s"
        data = (relacao.turmaId, relacao.diaSemanaId, relacao.horarioDeInicio, relacao.horarioDeTermino, relacao.id)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
