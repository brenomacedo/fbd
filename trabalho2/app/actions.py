import sys
sys.path.append("..")

from controllers.aluno_controller import AlunosController
from controllers.avaliacao_controller import AvaliacaoController
from controllers.campus_controller import CampusController
from controllers.centro_controller import CentroController
from controllers.curso_controller import CursoController
from controllers.details_controller import DetailsController
from controllers.disciplina_controller import DisciplinaController
from controllers.local_controller import LocalController
from controllers.professor_controller import ProfessorController
from controllers.reitor_controller import ReitorController
from controllers.turma_controller import TurmaController
from controllers.relacao_alunos_turmas_controller import RelacaoAlunosTurmasController
from controllers.relacao_cursos_disciplinas_controller import RelacaoCursosDisciplinasController
from controllers.relacao_professores_disciplinas_controller import RelacaoProfessoresDisciplinasController
from controllers.relacao_turmas_dias_semana_controller import RelacaoTurmasDiasSemanaController

alunosController = AlunosController()
avaliacaoController = AvaliacaoController()
campusController = CampusController()
centroController = CentroController()
cursoController = CursoController()
detailsController = DetailsController()
disciplinaController = DisciplinaController()
localController = LocalController()
professorController = ProfessorController()
reitorController = ReitorController()
turmaController = TurmaController()
relacaoAlunosTurmasController = RelacaoAlunosTurmasController()
relacaoCursosDisciplinasController = RelacaoCursosDisciplinasController()
relacaoProfessorDisciplinasController = RelacaoProfessoresDisciplinasController()
relacaoTurmasDiasSemanaController = RelacaoTurmasDiasSemanaController()


actions = {
    1: {
        1: alunosController.createAluno,
        2: avaliacaoController.createAvaliacao,
        3: campusController.createCampus,
        4: centroController.createCentro,
        5: cursoController.createCurso,
        6: disciplinaController.createDisciplina,
        7: localController.createLocal,
        8: professorController.createProfessor,
        9: reitorController.createReitor,
        10: turmaController.createTurma,
        11: relacaoAlunosTurmasController.createRelacaoAlunosTurmas,
        12: relacaoCursosDisciplinasController.createRelacaoCursosDisciplinas,
        13: relacaoProfessorDisciplinasController.createRelacaoProfessoresDisciplinas,
        14: relacaoTurmasDiasSemanaController.createRelacaoTurmasDiasSemana
    },
    2: {
        1: alunosController.readAluno,
        2: avaliacaoController.readAvaliacao,
        3: campusController.readCampus,
        4: centroController.readCentro,
        5: cursoController.readCurso,
        6: disciplinaController.readDisciplina,
        7: localController.readLocal,
        8: professorController.readProfessor,
        9: reitorController.readReitor,
        10: turmaController.readTurma,
        11: relacaoAlunosTurmasController.readRelacaoAlunosTurmas,
        12: relacaoCursosDisciplinasController.readRelacaoCursosDisciplinas,
        13: relacaoProfessorDisciplinasController.readRelacaoProfessoresDisciplinas,
        14: relacaoTurmasDiasSemanaController.readRelacaoTurmasDiasSemana
    },
    3: {
        1: alunosController.updateAluno,
        2: avaliacaoController.updateAvaliacao,
        3: campusController.updateCampus,
        4: centroController.updateCentro,
        5: cursoController.updateCurso,
        6: disciplinaController.updateDisciplina,
        7: localController.updateLocal,
        8: professorController.updateProfessor,
        9: reitorController.updateReitor,
        10: turmaController.updateTurma,
        11: relacaoAlunosTurmasController.updateRelacaoAlunosTurmas,
        12: relacaoCursosDisciplinasController.updateRelacaoCursosDisciplinas,
        13: relacaoProfessorDisciplinasController.updateRelacaoProfessoresDisciplinas,
        14: relacaoTurmasDiasSemanaController.updateRelacaoTurmasDiasSemana
    },
    4: {
        1: alunosController.deleteAluno,
        2: avaliacaoController.deleteAvaliacao,
        3: campusController.deleteCampus,
        4: centroController.deleteCentro,
        5: cursoController.deleteCurso,
        6: disciplinaController.deleteDisciplina,
        7: localController.deleteLocal,
        8: professorController.deleteProfessor,
        9: reitorController.deleteReitor,
        10: turmaController.deleteTurma,
        11: relacaoAlunosTurmasController.deleteRelacaoAlunosTurmas,
        12: relacaoCursosDisciplinasController.deleteRelacaoCursosDisciplinas,
        13: relacaoProfessorDisciplinasController.deleteRelacaoProfessoresDisciplinas,
        14: relacaoTurmasDiasSemanaController.deleteRelacaoTurmasDiasSemana
    },
    5: {
        1: detailsController.consultarMediasDaTurma,
        2: detailsController.consultarTurmasDeUmSemestre,
        3: detailsController.consultarLocaisEmUmBloco,
        4: detailsController.consultarTurmasEmUmLocal,
        5: detailsController.consultarHistoricoEscolar
    }
}