from .actions import actions

def menu():
    print('================== TRABALHO 2 ====================')
    print('Digite uma opção de operação')
    print('1 - CREATE')
    print('2 - READ')
    print('3 - UPDATE')
    print('4 - DELETE')
    print('5 - CONSULTA ESPECIFICA')
    print('0 - SAIR')
    get = True
    opcao1 = None
    opcao2 = None
    while get:
        try:
            opcao1 = int(input('Digite a opção desejada: '))
            if opcao1 > 5 or opcao1 < 0:
                raise Exception()

            if opcao1 == 5:
                print('Digite a consulta específica que deseja: ')
                print('1 - Consultar médias da turma')            
                print('2 - Consultar turmas de um semestre')            
                print('3 - Consultar locais em um bloco')            
                print('4 - Consultar turmas em um local')            
                print('5 - Consutar historico escolar')
                get2 = True
                while get2:
                    try:
                        opcao2 = int(input('Digite a opção desejada: '))
                        if opcao2 > 5 or opcao2 < 1:
                            raise Exception()

                        return (opcao1, opcao2)
                    except:
                        print('Opção inválida')
            elif opcao1 == 0:
                return (opcao1, 0)
            else:
                print('Digite a tabela que deseja realizar a operação escolhida: ')
                print('1 - alunos')
                print('2 - avaliacoes')
                print('3 - campi')
                print('4 - centros')
                print('5 - cursos')
                print('6 - disciplinas')
                print('7 - locais')
                print('8 - professores')
                print('9 - reitores')
                print('10 - turmas')
                print('11 - relacao_alunos_turmas')
                print('12 - relacao_cursos_disciplinas')
                print('13 - relacao_professores_disciplinas')
                print('14 - relacao_turmas_diassemana')
                get2 = True
                while get2:
                    try:
                        opcao2 = int(input('Digite a opção desejada: '))
                        if opcao2 > 14 or opcao2 < 1:
                            raise Exception()

                        return opcao1, opcao2
                    except:
                        print('Opção inválida')

        except:
            print('Opção inválida')


def app():
    run = True
    while run:
        option = menu()
        if option[0] == 0:
            run = False
        else:
            option1 = option[0]
            option2 = option[1]
            actions[option1][option2]()
