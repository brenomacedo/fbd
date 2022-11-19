import sys
sys.path.append("..")

from models.reitor import Reitor
from .repository import Repository

class ReitorRepository(Repository):
    def create(self, reitor: Reitor):
        SQL = "INSERT INTO reitores (dataDeAdmissao, professorId) VALUES (%s, %s)"
        data = (reitor.dataDeAdmissao, reitor.professorId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT id, dataDeAdmissao, professorId FROM reitores"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        reitores = Reitor.fromArray(resultado)
        return reitores

    def delete(self, id: int):
        SQL = "DELETE FROM reitores WHERE id = %s"
        data = (id,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, reitor: Reitor):
        SQL = "UPDATE reitores SET dataDeAdmissao = %s, professorId = %s WHERE id = %s"
        data = (reitor.dataDeAdmissao, reitor.professorId, reitor.id)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
