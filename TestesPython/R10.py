import Testes_Validacao as tests
#testes de validação
def testesLocadora():

    print('bateria testes de validacao em locadora:')

    print('testes com tuplas validas:')

    for i in range(1,4):
        print('teste: '+str(i))
        tests.test_valid_locadora()
        print('\n')

    print('fim dos testes com tuplas validas! \n')

def testesCliente():
    print('bateria testes de validacao em cliente:')

    print('testes com tuplas validas:')

    for i in range(1,4):
        print('teste: '+str(i))
        tests.test_valid_cliente()
        print('\n')

    print('fim dos testes com tuplas validas! \n')

def testesLocacao():
    print('bateria testes de validacao em locacao:')

    print('testes com tuplas validas:')

    for i in range(1,4):
        print('teste: '+str(i))
        tests.test_valid_locacao()
        print('\n')

    print('fim dos testes com tuplas validas! \n')


testesLocadora()
testesCliente()
