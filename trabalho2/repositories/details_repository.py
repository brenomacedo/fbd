import sys
sys.path.append("..")

from .repository import Repository
from models.aluno import Aluno
from models.avaliacao import Avaliacao
from models.turma import Turma
from models.local import Local
from models.disciplina import Disciplina
from models.dias_semana import DiasSemana
from models.relacao_turmas_dias_semana import RelacaoTurmasDiasSemana

class DetailsRepository(Repository):
    def indexMediaDosAlunosDeUmaTurma(self, turmaId: int):
        SQL = "SELECT AL.matricula, AL.nome, AVG(AV.nota) FROM avaliacoes AS AV\
            INNER JOIN relacao_alunos_turmas RAT ON AV.alunosturmasid = RAT.id\
                INNER JOIN alunos AL ON AL.matricula = RAT.alunoid\
                    INNER JOIN turmas T ON T.codigo = RAT.turmaid\
                        WHERE T.estado = 'concluida' AND T.codigo = %s GROUP BY AL.matricula, AL.nome"

        data = (turmaId,)
        self.cursor.execute(SQL, data)
        tuplasDeNotas = self.cursor.fetchall()
        notas = []
        for nota in tuplasDeNotas:
            aluno = Aluno()
            aluno.matricula = nota[0]
            aluno.nome = nota[1]

            avaliacao = Avaliacao()
            avaliacao.nota = nota[2]
            notas.append((aluno, avaliacao))
        return notas

    def indexTurmasDeUmSemestre(self, semestre: str):
        SQL = "SELECT codigo, periodo, estado, disciplinaId, localId, alunosMatriculados, capacidade FROM turmas WHERE periodo = %s"
        data = (semestre,)
        self.cursor.execute(SQL, data)
        tuplasDeTurmas = self.cursor.fetchall()

        turmas = Turma.fromArray(tuplasDeTurmas)
        return turmas

    def locaisEmUmBloco(self, bloco: int):
        SQL = "SELECT codigo, nome, bloco, lotacao, descricao, tipo, centroid FROM locais WHERE bloco = %s"
        data = (bloco,)
        self.cursor.execute(SQL, data)
        tuplasDeLocais = self.cursor.fetchall()

        locais = Local.fromArray(tuplasDeLocais)
        return locais
        
    def turmasEmUmLocal(self, localId: int):
        SQL = "SELECT T.codigo AS turmaCodigo, D.codigo AS disciplinaCodigo, D.nome FROM turmas T\
            INNER JOIN disciplinas D ON D.codigo = T.disciplinaId WHERE localId = %s"
        data = (localId,)
        self.cursor.execute(SQL, data)
        tuplasDeTurmas = self.cursor.fetchall()
        turmas = []

        for turma in tuplasDeTurmas:
            novaTurma = Turma()
            novaTurma.codigo = turma[0]
            novaDisciplina = Disciplina()
            novaDisciplina.codigo = turma[1]
            novaDisciplina.nome = turma[2]

            SQL = "SELECT R.horariodeinicio, R.horariodetermino, D.dia FROM relacao_turmas_diassemana R\
                INNER JOIN diasSemana D ON R.diasemanaid = D.id WHERE turmaId = %s"
            data = (novaTurma.codigo,)
            self.cursor.execute(SQL, data)

            tuplasDeDiasEHorarios = self.cursor.fetchall()
            diasEHorarios = []

            for diaEHorario in tuplasDeDiasEHorarios:
                novoDia = DiasSemana()
                novoDia.dia = diaEHorario[2]
                novoHorario = RelacaoTurmasDiasSemana()
                novoHorario.horarioDeInicio = diaEHorario[0].strftime('%H:%M:%S')
                novoHorario.horarioDeTermino = diaEHorario[1].strftime('%H:%M:%S')
                diasEHorarios.append((novoDia, novoHorario))

            turmas.append((novaTurma, novaDisciplina, diasEHorarios))

        return turmas
        
    def historicoEscolar(self, matricula: int):
        SQL = "SELECT T.codigo, AVG(AV.nota) FROM relacao_alunos_turmas RAT\
        INNER JOIN turmas T ON T.codigo = RAT.turmaid\
        INNER JOIN alunos AL ON AL.matricula = RAT.alunoid\
        INNER JOIN avaliacoes AV ON AV.alunosturmasid = RAT.id\
        WHERE AL.matricula = %s\
        GROUP BY AL.matricula, AL.nome, T.codigo"
        data = (matricula,)

        self.cursor.execute(SQL, data)
        historico = self.cursor.fetchall()

        medias = []
        for media in historico:
            novaTurma = Turma()
            novaAvaliacao = Avaliacao()
            novaTurma.codigo = media[0]
            novaAvaliacao.nota = media[1]
            medias.append((novaTurma, novaAvaliacao))

        return medias