-- ALUNOS

CREATE TYPE GENERO AS ENUM ('masculino', 'feminino', 'nao_binario', 'outro');
CREATE TYPE FORMACAO AS ENUM ('mestrado', 'doutorado');
CREATE TYPE TURMA_ESTADO AS ENUM ('aberta', 'concluida');
CREATE TYPE LOCAL_TIPO AS ENUM ('bloco', 'sala_de_aula', 'auditorio', 'laboratorio');
CREATE TYPE DIAS_SEMANA AS ENUM ('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado');
CREATE TYPE TIPO_AVALIACAO AS ENUM ('prova', 'trabalho');

CREATE TABLE alunos (
  matricula INTEGER PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  nascimento DATE,
  endereco VARCHAR(255),
  sexo GENERO,
  cursoId INTEGER NOT NULL
);

-- CURSOS

CREATE TABLE cursos (
  codigo INTEGER PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  cargaHoraria INTEGER,
  coordenadorId INTEGER NOT NULL,
  centroId INTEGER NOT NULL
);

-- DISCIPLINAS

CREATE TABLE disciplinas (
  codigo INTEGER PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  cargaHoraria INTEGER,
  ementa VARCHAR(255),
  CONSTRAINT cargaHoraria_intervalo CHECK (cargaHoraria >= 32 AND cargaHoraria <= 128)
);

-- PROFESSORES

CREATE TABLE professores (
  codigo INTEGER PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  sexo GENERO,
  formacao FORMACAO NOT NULL,
  nascimento DATE
);

-- CENTROS

CREATE TABLE centros (
  codigo INTEGER PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  campusId INTEGER NOT NULL,
  diretorId INTEGER NOT NULL
);

-- CAMPUS

CREATE TABLE campi (
  codigo INTEGER PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  localizacao VARCHAR(255) NOT NULL,
  indicadoPor INTEGER NOT NULL
);

-- REITORES

CREATE TABLE reitores (
  id SERIAL PRIMARY KEY,
  dataDeAdmissao DATE,
  professorId INTEGER NOT NULL
);

-- TURMAS

CREATE TABLE turmas (
  codigo INTEGER PRIMARY KEY,
  periodo VARCHAR(7), -- ____._
  estado TURMA_ESTADO,
  disciplinaId INTEGER NOT NULL,
  localId INTEGER NOT NULL,
  alunosMatriculados INTEGER NOT NULL DEFAULT 0,
  capacidade INTEGER NOT NULL DEFAULT 60,
  CONSTRAINT capacidadeMaxima CHECK (alunosMatriculados <= capacidade)
);

-- LOCAIS

CREATE TABLE locais (
  codigo INTEGER PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  bloco INTEGER,
  lotacao INTEGER NOT NULL,
  descricao VARCHAR(255),
  tipo LOCAL_TIPO,
  centroId INTEGER NOT NULL
);

CREATE TABLE avaliacoes (
  id SERIAL PRIMARY KEY,
  nota REAL NOT NULL,
  tipo TIPO_AVALIACAO NOT NULL,
  CONSTRAINT avaliacao_intervalo CHECK (nota >= 0 AND nota <= 10),
  alunosTurmasId INTEGER NOT NULL
);

-- RELACAO CURSA: ALUNOS -- N:1 -- CURSOS

ALTER TABLE alunos
	ADD CONSTRAINT fk_curso_aluno FOREIGN KEY (cursoId)
    REFERENCES cursos ON DELETE CASCADE;
    
-- RELACAO REALIZA: ALUNOS -- N:N -- TURMAS

CREATE TABLE relacao_alunos_turmas (
  id SERIAL PRIMARY KEY,
  alunoId INTEGER NOT NULL,
  turmaId INTEGER NOT NULL,
  UNIQUE (alunoId, turmaId),
  CONSTRAINT fk_aluno FOREIGN KEY (alunoId) REFERENCES alunos ON DELETE CASCADE,
  CONSTRAINT fk_turma FOREIGN KEY (turmaId) REFERENCES turmas ON DELETE CASCADE
);

-- RELACAO PERTENCE A: CURSOS -- N:N -- DISCIPLINAS

CREATE TABLE relacao_cursos_disciplinas (
  id SERIAL PRIMARY KEY,
  cursoId INTEGER NOT NULL,
  disciplinaId INTEGER NOT NULL,
  UNIQUE (cursoId, disciplinaId),
  CONSTRAINT fk_curso FOREIGN KEY (cursoId) REFERENCES cursos ON DELETE CASCADE,
  CONSTRAINT fk_disciplina FOREIGN KEY (disciplinaId) REFERENCES disciplinas ON DELETE CASCADE
);

-- RELACAO POSSUI: AVALIACAO -- N:1 -- RELACAO_ALUNOS_TURMAS

ALTER TABLE avaliacoes
	ADD CONSTRAINT fk_alunos_turmas_id FOREIGN KEY (alunosTurmasId)
    REFERENCES relacao_alunos_turmas ON DELETE CASCADE;

-- RELACAO COORDENA: CURSOS -- 1:1 -- PROFESSORES

ALTER TABLE cursos
	ADD CONSTRAINT fk_curso_coordenador FOREIGN KEY (coordenadorId)
    	REFERENCES professores ON DELETE CASCADE;
        
-- RELACAO FAZ PARTE DE: CURSOS N:1 CENTROS
ALTER TABLE cursos
	ADD CONSTRAINT fk_curso_centro FOREIGN KEY (centroId)
    	REFERENCES centros ON DELETE CASCADE;
   
    
-- RELACAO LECIONA: PROFESSRES N:N DISCIPLINAS

CREATE FUNCTION verificaDisciplinas (profId INTEGER)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS
$$
DECLARE
	quantidadeDisciplinas INTEGER;
BEGIN
	SELECT COUNT(*) INTO quantidadeDisciplinas FROM relacao_professores_disciplinas WHERE professorId = profId;
    RETURN quantidadeDisciplinas <= 4;
END;
$$;

CREATE TABLE relacao_professores_disciplinas (
  id SERIAL PRIMARY KEY,
  professorId INTEGER NOT NULL,
  disciplinaId INTEGER NOT NULL,
  UNIQUE (professorId, disciplinaId),
  CONSTRAINT fk_professor FOREIGN KEY (professorId) REFERENCES professores ON DELETE CASCADE,
  CONSTRAINT fk_disciplina FOREIGN KEY (disciplinaId) REFERENCES disciplinas ON DELETE CASCADE,
  CONSTRAINT maximo_disciplinas CHECK (verificaDisciplinas (professorId))
);

-- RELACAO É PROFESSOR: REITORES 1:1 PROFESSORES

ALTER TABLE reitores
	ADD CONSTRAINT fk_professor FOREIGN KEY (professorId)
    REFERENCES professores ON DELETE CASCADE;
    
-- RELACAO POSSUI: TURMAS N:1 DISCIPLINAS

ALTER TABLE turmas
	ADD CONSTRAINT fk_disciplina FOREIGN KEY (disciplinaId)
    	REFERENCES disciplinas ON DELETE CASCADE;

-- RELACAO POSSUI: TURMAS N:1 LOCAL

ALTER TABLE turmas
	ADD CONSTRAINT fk_local FOREIGN KEY (localId)
    	REFERENCES locais ON DELETE CASCADE;

-- RELACAO POSSUI: TURMAS N:N DIAS DA SEMANA

CREATE TABLE diasSemana (
  id SERIAL PRIMARY KEY,
  dia DIAS_SEMANA UNIQUE
);

INSERT INTO diasSemana (dia) VALUES ('segunda');
INSERT INTO diasSemana (dia) VALUES ('terca');
INSERT INTO diasSemana (dia) VALUES ('quarta');
INSERT INTO diasSemana (dia) VALUES ('quinta');
INSERT INTO diasSemana (dia) VALUES ('sexta');
INSERT INTO diasSemana (dia) VALUES ('sabado');

CREATE TABLE relacao_turmas_diasSemana (
  id SERIAL PRIMARY KEY,
  turmaId INTEGER NOT NULL,
  diaSemanaId INTEGER NOT NULL,
  UNIQUE (turmaId, diaSemanaId),
  horarioDeInicio TIME NOT NULL,
  horarioDeTermino TIME NOT NULL,
  CONSTRAINT fk_turma FOREIGN KEY (turmaId) REFERENCES turmas ON DELETE CASCADE,
  CONSTRAINT fk_diaSemana FOREIGN KEY (diaSemanaId) REFERENCES diasSemana ON DELETE CASCADE
);

-- RELACAO PERTENCE A: LOCAIS N:1 CENTROS

ALTER TABLE locais
	ADD CONSTRAINT fk_centro FOREIGN KEY (centroId)
    	REFERENCES centros ON DELETE CASCADE;
        
-- RELACAO DIRIGE: PROFESSORES 1:1 CENTROS

ALTER TABLE centros
	ADD CONSTRAINT fk_diretor FOREIGN KEY (diretorId)
    REFERENCES professores ON DELETE SET NULL;
    
-- RELACAO PERTENCE A: CENTRO N:1 CAMPI

ALTER TABLE centros
	ADD CONSTRAINT fk_campus FOREIGN KEY (campusId)
    REFERENCES campi ON DELETE CASCADE;
    
-- RELACAO INDICADO POR: CAMPI N:1 REITOR

ALTER TABLE campi
	ADD CONSTRAINT fk_reitor FOREIGN KEY (indicadoPor)
    REFERENCES reitores ON DELETE CASCADE;
    
-- TRIGGERS

-- Os alunos não podem fazer turmas de mesmas disciplinas

CREATE FUNCTION checkAlunosDisciplinasRepetidas() RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
DECLARE
	disciplinaInserida INTEGER;
BEGIN
	SELECT disciplinaId INTO disciplinaInserida FROM turmas WHERE turmas.codigo = NEW.turmaId;
    
    IF EXISTS (
      	SELECT * FROM relacao_alunos_turmas
    	INNER JOIN turmas ON turmas.codigo = relacao_alunos_turmas.turmaId
    	WHERE relacao_alunos_turmas.alunoId = NEW.alunoId AND turmas.disciplinaId = disciplinaInserida
    ) THEN
    	RAISE EXCEPTION 'Já existe uma turma com essa disciplina';
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER alunosDisciplinasRepetidas BEFORE INSERT OR UPDATE ON relacao_alunos_turmas
FOR EACH ROW EXECUTE FUNCTION checkAlunosDisciplinasRepetidas();


-- Um professor pode coordenar somente um curso ou dirigir somente um centro

CREATE FUNCTION checkCursoMaisDeUmCoordenador() RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
	IF EXISTS (
      SELECT * FROM cursos WHERE coordenadorId = NEW.coordenadorId
    ) THEN
    	RAISE EXCEPTION 'O professor que coordena esse curso já coordena outro curso!';
    END IF;
    
    IF EXISTS (
      SELECT * FROM centros WHERE diretorId = NEW.coordenadorId
    ) THEN
    	RAISE EXCEPTION 'O professor que coordena esse curso já dirige outro centro!';
    END IF;
    
    RETURN NEW;
END;
$$;

CREATE TRIGGER cursoMaisDeUmCoordenador BEFORE INSERT OR UPDATE ON cursos
FOR EACH ROW EXECUTE FUNCTION checkCursoMaisDeUmCoordenador();



CREATE FUNCTION checkCentroMaisDeUmDiretor() RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
	IF EXISTS (
      SELECT * FROM cursos WHERE coordenadorId = NEW.diretorId
    ) THEN
    	RAISE EXCEPTION 'O professor que dirige esse centro já coordena outro curso!';
    END IF;

    IF EXISTS (
      SELECT * FROM centros WHERE diretorId = NEW.diretorId
    ) THEN
    	RAISE EXCEPTION 'O professor que dirige esse centro já dirige outro centro!';
    END IF;
    
    RETURN NEW;
END;
$$;

CREATE TRIGGER centroMaisDeUmDiretor BEFORE INSERT OR UPDATE ON centros
FOR EACH ROW EXECUTE FUNCTION checkCentroMaisDeUmDiretor();

-- Incrementar alunos matriculados nas turmas ao adicionar um aluno

CREATE FUNCTION incrementarAlunosFunc() RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
	UPDATE turmas SET alunosMatriculados = alunosMatriculados + 1 WHERE turmas.codigo = NEW.turmaId;
    RETURN NULL;
END;
$$;

CREATE TRIGGER incrementarAlunos AFTER INSERT ON relacao_alunos_turmas
FOR EACH ROW EXECUTE FUNCTION incrementarAlunosFunc();


CREATE FUNCTION decrementarAlunosFunc() RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
	UPDATE turmas SET alunosMatriculados = alunosMatriculados - 1 WHERE turmas.codigo = NEW.turmaId;
    RETURN NULL;
END;
$$;

CREATE TRIGGER decrementarAlunos AFTER INSERT ON relacao_alunos_turmas
FOR EACH ROW EXECUTE FUNCTION decrementarAlunosFunc();
