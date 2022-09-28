-- Inserindo campus --------------------

INSERT INTO campi (codigo, nome, localizacao) VALUES (69420, 'Campus do Pici', 'Fortaleza');
INSERT INTO campi (codigo, nome, localizacao) VALUES (111111, 'Campus de Sobral', 'Sobral');
INSERT INTO campi (codigo, nome, localizacao) VALUES (444444, 'Campus do Quixada', 'Quixada');

-- Inserindo professores --------------------

INSERT INTO professores (codigo, nome, email, sexo, formacao, nascimento)
VALUES (13, 'Javam de Castro Machado', 'javam@ufc.br', 'masculino', 'doutorado', '1972-02-22');

INSERT INTO professores (codigo, nome, email, sexo, formacao, nascimento)
VALUES (22, 'Joaquim Bento Cavalcante Neto', 'joaquimb@dc.ufc.br', 'masculino', 'doutorado', '1984-09-11');

INSERT INTO professores (codigo, nome, email, sexo, formacao, nascimento)
VALUES (123, 'Creto Augusto Vidal', 'cvidal@lia.ufc.br ', 'masculino', 'doutorado', '1970-09-11');

INSERT INTO professores (codigo, nome, email, sexo, formacao, nascimento)
VALUES (10, 'Pablo Mayckon Silva Farias', 'pablo@dc.ufc.br ', 'masculino', 'doutorado', '1990-09-12');

-- Inserindo centros --------------------

INSERT INTO centros (codigo, nome, campusId, diretorId) VALUES (69, 'Centro de Ciências', 69420, 13);
INSERT INTO centros (codigo, nome, campusId, diretorId) VALUES (70, 'Centro de Tecnologia', 69420, 22);

-- Inserindo disciplinas

INSERT INTO disciplinas (codigo, nome, cargaHoraria, ementa) VALUES (123, 'Felicidade', 64, 'Você será feliz nessa disciplina (eu acho)');
INSERT INTO disciplinas (codigo, nome, cargaHoraria, ementa) VALUES (555, 'Computação Gráfica', 64, 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk');
INSERT INTO disciplinas (codigo, nome, cargaHoraria, ementa) VALUES (444, 'Fundamentos de Banco de Dados', 64, 'Professor Javam gente boa');

INSERT INTO relacao_professores_disciplinas (professorId, disciplinaId) VALUES (123, 123);
INSERT INTO relacao_professores_disciplinas (professorId, disciplinaId) VALUES (123, 555);
INSERT INTO relacao_professores_disciplinas (professorId, disciplinaId) VALUES (13, 444);
INSERT INTO relacao_professores_disciplinas (professorId, disciplinaId) VALUES (22, 444);

-- Inserindo locais

INSERT INTO locais (codigo, nome, bloco, lotacao, descricao, tipo, centroId)
VALUES (12345, 'Bloco da Computação - 910', NULL, 100, 'Bloco da computação, onde tem a sala do PET, ar condicionado mt bom', 'bloco', 69);

INSERT INTO locais (codigo, nome, bloco, lotacao, descricao, tipo, centroId)
VALUES (12346, 'LEC', 910, 40, 'Laboratório de Computação, só no compiuter', 'laboratorio', 69);

INSERT INTO locais (codigo, nome, bloco, lotacao, descricao, tipo, centroId)
VALUES (12347, 'Sala 1045', 915, 40, 'Sala de aula do bloco 915 - Antiga sala do juvencio', 'sala_de_aula', 69);

INSERT INTO locais (codigo, nome, bloco, lotacao, descricao, tipo, centroId)
VALUES (12348, 'Auditorio do 915', 915, 50, 'Auditorio do 915, aquele lugar tem uma acustica horrivel :(', 'auditorio', 69);

-- Inserindo o reitor

INSERT INTO reitores (dataDeAdmissao, professorId) VALUES ('2022-02-22', 10);

-- Inserindo cursos

INSERT INTO cursos (codigo, nome, cargaHoraria, coordenadorId, centroId) VALUES (6551, 'Ciência da Computação', 3000, 10, 69);
INSERT INTO cursos (codigo, nome, cargaHoraria, coordenadorId, centroId) VALUES (3213, 'Biologia', 3000, 13, 69);

INSERT INTO relacao_cursos_disciplinas (cursoId, disciplinaId) VALUES (3213, 123);
INSERT INTO relacao_cursos_disciplinas (cursoId, disciplinaId) VALUES (6551, 123);
INSERT INTO relacao_cursos_disciplinas (cursoId, disciplinaId) VALUES (6551, 555);
INSERT INTO relacao_cursos_disciplinas (cursoId, disciplinaId) VALUES (6551, 444);

-- Inserindo turmas

INSERT INTO turmas (codigo, periodo, estado, disciplinaId, localId) VALUES (321, '2022.2', 'aberta', 123, 12347);
INSERT INTO turmas (codigo, periodo, estado, disciplinaId, localId) VALUES (123, '2022.2', 'aberta', 555, 12347);

INSERT INTO relacao_turmas_diasSemana (turmaId, diaSemanaId, horarioDeInicio, horarioDeTermino) VALUES (321, 2, '08:00', '12:00');
INSERT INTO relacao_turmas_diasSemana (turmaId, diaSemanaId, horarioDeInicio, horarioDeTermino) VALUES (123, 1, '10:00', '12:00');
INSERT INTO relacao_turmas_diasSemana (turmaId, diaSemanaId, horarioDeInicio, horarioDeTermino) VALUES (123, 3, '10:00', '12:00');

-- Inserindo alunos

INSERT INTO alunos (matricula, nome, email, nascimento, endereco, sexo, cursoId)
VALUES (508682, 'Renan Xerez Marques', 'renanxerez@gmail.com', '2003-05-10', 'Avenida Paulo Muzy Numero 22', 'masculino', 6551);

INSERT INTO alunos (matricula, nome, email, nascimento, endereco, sexo, cursoId)
VALUES (123456, 'Maria Eduarda Leandro', 'mariaeduarda@gmail.com', '2003-12-22', 'Rua dos bobos Numero 0', 'nao_binario', 3213);

INSERT INTO alunos (matricula, nome, email, nascimento, endereco, sexo, cursoId)
VALUES (514513, 'Breno Macêdo de Brito', 'brenomacedo@gmail.com', '2003-01-14', 'Avenida Brasil Numero 777', 'masculino', 6551);

INSERT INTO alunos (matricula, nome, email, nascimento, endereco, sexo, cursoId)
VALUES (508016, 'Gustavo Wendell Moreira Valença', 'gustavovalenca13@gmail.com', '2003-08-29', 'Rua Francesa Numero 92', 'masculino', 6551);

INSERT INTO alunos (matricula, nome, email, nascimento, endereco, sexo, cursoId)
VALUES (509298 , 'Tiago Brandão Forte', 'bigbrandon@gmail.com', '2003-05-10', 'ALDEOTA', 'masculino', 6551);

INSERT INTO relacao_alunos_disciplinas (alunoId, disciplinaId, avaliacao) VALUES (508682, 555, 4);
INSERT INTO relacao_alunos_disciplinas (alunoId, disciplinaId, avaliacao) VALUES (123456, 123, 10);
INSERT INTO relacao_alunos_disciplinas (alunoId, disciplinaId, avaliacao) VALUES (514513, 555, 4);
INSERT INTO relacao_alunos_disciplinas (alunoId, disciplinaId, avaliacao) VALUES (508016, 555, 7);
INSERT INTO relacao_alunos_disciplinas (alunoId, disciplinaId, avaliacao) VALUES (509298, 555, 10);

