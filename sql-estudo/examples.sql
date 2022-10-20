-- o formato de uma consulta sql é:
-- SELECT [ DISTINCT ] lista-selecao
-- FROM lista-from
-- WHERE qualificacao

-- exemplo: encontrar todos os nomes e idades dos marinheiros
SELECT DISTINCT M."nome-main", M.idade
FROM Marinheiros AS M
-- nesse exemplo, o DISTINCT serve
-- para selecionar as tuplas diferentes, sem
-- repetição de tuplas idênticas


-- exemplo2: encontrar todos os marinheiros com uma avaliação acima de 7
SELECT M."id-marin", M."nome-marin", M.avaliacao,
       M.idade
FROM Marinheiros AS M
WHERE M.avaliacao > 7

-- exemplo3: outras consultas

SELECT nome-main
FROM Marinheiros AS M, Reservas AS R
WHERE M."id-marin" = R."id-marin" AND R."id-barco" = 103

SELECT nome-marin
FROM Marinheiros, Reservas
WHERE Marinheiros."id-marin" = Reservas."id-marin"
      AND id-barco = 103

-- exemplo4: operador diferente (<>) ou (!=)
-- e expressões no comando SELECT e WHERE
SELECT M."nome-marin", M.avaliacao + 1 AS avaliacao,
FROM Marinheiros AS M, Reservas AS R1, Reservas AS R2,
WHERE M."id-marin" = R1."id-marin"
AND M."id-marin" = R2."id-marin"
AND R1."dia" = R2."dia" AND R1."id-barco" <> R2."id-barco"

SELECT M1."nome-marin" AS nome1, M2."nome-marin" AS nome2
FROM Marinheiros AS M1, Marinheiros M2
WHERE 2*M1."avaliacao" = M2."avaliacao" - 1

-- exemplo5: UNION, INTERSECT E EXCEPT
-- equivalentes as operações de teoria dos conjuntos,
-- União, Interseção e Subtração

SELECT M."nome-marin"
FROM Marinheiros AS M, Reservas AS R, Barcos AS B
WHERE M."id-marin" = R."id-marin"
AND R."id-barco" = B."id-barco"
AND B.cor = 'vermelho'
UNION -- uniao entre dois conjuntos
SELECT M2."nome-marin"
FROM Marinheiros AS M2, Barcos AS B2, Reservas AS R2
WHERE M2."id-marin" = R2."id-marin" AND
R2."id-barco" = B2."id-barco" AND B2.cor = 'verde'

SELECT M."nome-marin"
FROM Marinheiros AS M, Reservas AS R, Barcos AS B
WHERE M."id-marin" = R."id-marin"
AND R."id-barco" = B."id-barco"
AND B.cor = 'vermelho'
INTERSECT -- interseção entre dois conjuntos
SELECT M2."nome-marin"
FROM Marinheiros AS M2, Barcos AS B2, Reservas AS R2
WHERE M2."id-marin" = R2."id-marin" AND
R2."id-barco" = B2."id-barco" AND B2.cor = 'verde'

SELECT M."nome-marin"
FROM Marinheiros AS M, Reservas AS R, Barcos AS B
WHERE M."id-marin" = R."id-marin"
AND R."id-barco" = B."id-barco"
AND B.cor = 'vermelho'
EXCEPT -- subtracao entre dois conjuntos
SELECT M2."nome-marin"
FROM Marinheiros AS M2, Barcos AS B2, Reservas AS R2
WHERE M2."id-marin" = R2."id-marin" AND
R2."id-barco" = B2."id-barco" AND B2.cor = 'verde'

-- exemplo6: Essas operações eliminam tuplas
-- duplicadas, usar ALL após a operação para
-- reter as duplicatas

SELECT * FROM tabela1
UNION ALL (SELECT * FROM tablea2)

SELECT * FROM teste1
EXCEPT ALL (SELECT * FROM teste2)

SELECT * FROM table1
INTERSECT ALL (SELECT * FROM table2)

-- exemplo7: operador IN para verificar se uma tupla
-- pertence a um conjunto de tuplas
-- PENSAR NAS OPRAÇÕES COMO SE FOSSEM CONJUNTOS DE TUPLAS

SELECT M."nome-marin"
FROM Marinheiros AS M
WHERE M."id-marin" IN (
    SELECT R."id-marin" FROM Reservas AS R
    WHERE R."id-barco" IN (
        SELECT B."id-barco"
        FROM Barcos AS B
        WHERE B."cor" = 'vermelho'
    )
)

-- exemplo8: operador NOT IN também é válido!
SELECT M."nome-marin"
FROM Marinheiros AS M
WHERE M."id-marin" NOT IN (
    SELECT R."id-marin" FROM Reservas AS R
    WHERE R."id-barco" NOT IN (
        SELECT B."id-barco"
        FROM Barcos AS B
        WHERE B."cor" = 'vermelho'
    )
)

-- exemplo9: o operador EXISTS verifica se
-- um conjunto é não-vazio, observe também
-- que nesse exemplo, a consulta interna
-- é dependente da consulta externa
SELECT M."nome-marin"
FROM Marinheiros AS M
WHERE EXISTS ( -- NOT EXISTS também é válido
    SELECT * FROM Reservas AS R
    WHERE R."id-barco" = 103
    AND "R.id-marin" = M."id-marin"
)

-- exemplo10: em contrapartida com o EXISTS,
-- o operador UNIQUE verifica se o resultado
-- da consulta possui apenas valores que não se 
-- repetem, ou seja, ele retorna TRUE se nenhuma
-- linha aparecer duas vezes na resposta
-- da subconsulta (também há a versão NOT UNIQUE)
SELECT M."nome-marin"
FROM Marinheiros AS M
WHERE UNIQUE ( -- NOT UNIQUE também é válido
    SELECT * FROM Reservas AS R
    WHERE R."id-barco" = 103
    AND "R.id-marin" = M."id-marin"
)

-- exemplo11: operadores ANY e ALL
-- os operadores são equivalentes as
-- preposições EXISTE e PARA TODO,
-- inclusive nos casos de vacuidade
SELECT M."id-marin" FROM Marinheiros AS M
WHERE M.avaliacao > ANY (
    SELECT M2.avaliacao
    FROM Marinheiros AS M2
    WHERE M2."nome-marin" = 'Horatio'
)

SELECT M."id-marin" FROM Marinheiros AS M
WHERE M.avaliacao >= ALL (
    SELECT M2.avaliacao
    FROM Marinheiros AS M2
)

-- exemplo12: operadores agregados
-- pode-se usar o operador DISTINCT
-- para realizar a operações a apenas
-- valores distintos da coluna
SELECT AVG(DISTINCT M.idade)
FROM Marinheiros M

SELECT AVG (M.idade)
FROM Marinheiros AS M
WHERE M.avaliacao = 10

-- exemplo13: podemos usar o resultado de
-- uma seleção que possui uma coluna e um
-- unico elemento na comparação
SELECT M."nome-marin", M.idade
FROM Marinheiros AS M WHERE
(SELECT MAX(M2.idade) FROM Marinheiros AS M2) = M.idade
-- vicios de linguagem -- USAR OPERAÇÕES DE AGREGAÇÃO
-- NEM SEMPRE REQUEREM O USO DO GROUP BY

-- exemplo14: GROUP BY E HAVING
-- se o GROUP BY FOR omitido, a tabela inteira é 
-- considerada um grupo único
SELECT M.avaliacao, MIN(M.idade) AS minIdade
FROM Marinheiros AS M
WHERE M.idade >= 18
GROUP BY M.avaliacao
HAVING COUNT(*) > 1

-- exemplo15: EVERY E ANY
-- ao ter um agrupamento, podemos usar o EVERY
-- para filtrar os grupos selecionando somente
-- os grupos em que TODAS as tuplas satisfazem
-- um determinado predicado
-- o ANY é usado para selecionar apenas os grupos
-- em que ALGUMA tupla satisfaz o predicado
-- devem ser utilizadas na clausula HAVING
SELECT M.avaliacao, MIN(M.idade) AS minIdade
FROM Marinheiros AS M
WHERE M.idade >= 18
GROUP BY M.avaliacao
HAVING COUNT(*) > 1 AND EVERY (M.idade <= 60)
OR ANY (M.idade >= 15)

-- comparação de valores nulos
-- exemplo16: IS NULL para verificar se um valor
-- é nulo
SELECT nome FROM users WHERE
cidade IS NULL AND idade OR cidade IS NOT NULL

-- restrições de dominio
-- usar o CREATE DOMAIN para criar um dominio

CREATE DOMAIN avaliacaoVal INTEGER DEFAULT 1
CHECK (VALUE >= 1 AND VALUE <= 10)

CREATE TYPE avaliacao AS ('legal', 'medio', 'ruim')
-- assertivas: restrições não associadas a uma
-- tabela em particular

CREATE ASSERTION clubePequeno
CHECK (( SELECT COUNT (M.id-marin) FROM Marinheiros M)
+ ( SELECT COUNT (B.id-barco) FROM Barcos B )
< 100 )

-- triggers
CREATE TRIGGER cont-conj AFTER INSERT ON Alunos
REFERENCING NEW TABLE AS TuplasInseridas
FOR EACH STATEMENT
INSERT INTO
    ...

CREATE TRIGGER teste AFTER INSERT ON Alunos
DECLARE
    cont INTEGER;
BEGIN
    cont := 0;
END

CREATE TRIGGER teste2 AFTER INSERT ON Alunos
WHEN (new.idade < 18)
FOR EACH ROW
BEGIN
    cont := cont + 1;
END

-- no postgres:
-- CRIAR FUNCAO E INSERIR NO TRIGGER

CREATE FUNCTION emp_stamp() RETURNS TRIGGER AS
$body$
BEGIN
    IF NEW.empname IS NULL THEN
        RAISE EXCEPTION 'empname cannot be null';
    END IF

    RETURN NEW
END;
$body$
LANGUAGE plpgsql;

CREATE TRIGGER emp_stamp BEFORE INSERT OR UPDATE ON emp
FOR EACH ROW EXECUTE FUNCTION emp_stamp()
