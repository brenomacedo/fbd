import sys
sys.path.append("..")

from models.campus import Campus
from .repository import Repository

class CampusRepository(Repository):
    def create(self, campus: Campus):
        SQL = "INSERT INTO campi (codigo, nome, localizacao, indicadoPor) VALUES (%s, %s, %s, %s)"
        data = (campus.codigo, campus.nome, campus.localizacao, campus.indicadoPor)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT codigo, nome, localizacao, indicadoPor FROM campi"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        campi = Campus.fromArray(resultado)
        return campi

    def delete(self, codigo: int):
        SQL = "DELETE FROM campi WHERE codigo = %s"
        data = (codigo,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, campus: Campus):
        SQL = "UPDATE campi SET nome = %s, localizacao = %s, indicadoPor = %s WHERE codigo = %s"
        data = (campus.nome, campus.localizacao, campus.indicadoPor, campus.codigo)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None
