import Testes_Validacao as tests
#testes de validação
def testesLocadora():

    print('bateria testes de validacao em locadora:')

    print('testes com tuplas validas:')

    for i in range(1,3):
        print('teste: '+str(i))
        tests.test_valid_locadora()
        print('\n')

    print('fim dos testes com tuplas validas! \n')

    print('testes com tuplas invalidas:')

    for i in range(1,3):
        try:
            print('teste: '+str(i))
            tests.test_invalid_locadora()
            print('\n')
        except Exception as e:
            print("Ocorreu um erro:", e)
    print('fim dos testes com tuplas invalidas! \n')



def testesCliente():
    print('bateria testes de validacao em cliente:')

    print('testes com tuplas validas:')

    for i in range(1,3):
        print('teste: '+str(i))
        tests.test_valid_cliente()
        print('\n')

    print('fim dos testes com tuplas validas! \n')

    print('testes com tuplas invalidas:')

    for i in range(1,3):
        try:
            print('teste: '+str(i))
            tests.test_invalid_cliente()
            print('\n')
        except Exception as e:
            print("Ocorreu um erro:", e)
    print('fim dos testes com tuplas invalidas! \n')


def testesLocacao():
    print('bateria testes de validacao em locacao:')

    print('testes com tuplas validas:')

    for i in range(1,3):
        print('teste: '+str(i))
        tests.test_valid_locacao()
        print('\n')

    print('fim dos testes com tuplas validas! \n')

    print('testes com tuplas invalidas:')

    for i in range(1,3):
        try:
            print('teste: '+str(i))
            tests.test_invalid_locacao()
            print('\n')
        except Exception as e:
            print("Ocorreu um erro:", e)

    print('fim dos testes com tuplas invalidas! \n')



testesLocadora()
testesCliente()
testesLocacao()
