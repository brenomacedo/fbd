from models.relacao_cursos_disciplinas import RelacaoCursosDisciplinas
from repositories.relacao_cursos_disciplinas_repository import RelacaoCursosDisciplinasRepository

def main():
    professores = RelacaoCursosDisciplinasRepository().update(RelacaoCursosDisciplinas((5, 3213, 444)))
    # for professor in professores:
    #     print(professor)

if __name__ == '__main__':
    main()