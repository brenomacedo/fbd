import sys
sys.path.append("..")

from models.local import Local
from .repository import Repository

class LocalRepository(Repository):
    def create(self, local: Local):
        SQL = "INSERT INTO locais (codigo, nome, bloco, lotacao, descricao, tipo, centroId) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (local.codigo, local.nome, local.bloco, local.lotacao, local.descricao, local.tipo, local.centroId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT codigo, nome, bloco, lotacao, descricao, tipo, centroId FROM locais"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        locais = Local.fromArray(resultado)
        return locais

    def delete(self, codigo: int):
        SQL = "DELETE FROM locais WHERE codigo = %s"
        data = (codigo,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, local: Local):
        SQL = "UPDATE locais SET nome = %s, bloco = %s, lotacao = %s, descricao = %s, tipo = %s, centroId = %s WHERE codigo = %s"
        data = (local.nome, local.bloco, local.lotacao, local.descricao, local.tipo, local.centroId, local.codigo)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None