import sys
sys.path.append("..")

from database.database import databaseConnection
from models.centro import Centro
from .repository import Repository

class CentroRepository(Repository):
    def __init__(self):
        self.connection = databaseConnection.getConnection()
        self.cursor = databaseConnection.getCursor()

    def create(self, centro: Centro):
        SQL = "INSERT INTO centros (codigo, nome, campusId, diretorId) VALUES (%s, %s, %s, %s)"
        data = (centro.codigo, centro.nome, centro.campusId, centro.diretorId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT codigo, nome, campusId, diretorId FROM centros"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        centros = Centro.fromArray(resultado)
        return centros

    def delete(self, codigo: int):
        SQL = "DELETE FROM centros WHERE codigo = %s"
        data = (codigo,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
    
    def update(self, centro: Centro):
        SQL = "UPDATE centros SET nome = %s, campusId = %s, diretorId = %s WHERE codigo = %s"
        data = (centro.nome, centro.campusId, centro.diretorId, centro.codigo)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None