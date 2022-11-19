from models.relacao_turmas_dias_semana import RelacaoTurmasDiasSemana
from repositories.relacao_turmas_dias_semana_repository import RelacaoTurmasDiasSemanaRepository
from datetime import datetime

def main():
    professores = RelacaoTurmasDiasSemanaRepository().index()
    for professor in professores:
        print(professor)

if __name__ == '__main__':
    main()