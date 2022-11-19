import sys
sys.path.append("..")

from models.curso import Curso
from .repository import Repository

class CursoRepository(Repository):
    def create(self, curso: Curso):
        SQL = "INSERT INTO cursos (codigo, nome, cargaHoraria, coordenadorId, centroId) VALUES (%s, %s, %s, %s, %s)"
        data = (curso.codigo, curso.nome, curso.cargaHoraria, curso.coordenadorId, curso.centroId)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def index(self):
        SQL = "SELECT codigo, nome, cargaHoraria, coordenadorId, centroId FROM cursos"
        self.cursor.execute(SQL)
        resultado = self.cursor.fetchall()
        cursos = Curso.fromArray(resultado)
        return cursos

    def delete(self, codigo: int):
        SQL = "DELETE FROM cursos WHERE codigo = %s"
        data = (codigo,)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None

    def update(self, curso: Curso):
        SQL = "UPDATE cursos SET nome = %s, cargaHoraria = %s, coordenadorId = %s, centroId = %s WHERE codigo = %s"
        data = (curso.nome, curso.cargaHoraria, curso.coordenadorId, curso.centroId, curso.codigo)
        self.cursor.execute(SQL, data)
        self.connection.commit()
        return None