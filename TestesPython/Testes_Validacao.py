import unittest
import faker
import Webdriver_Utils as wb


def test_valid_locadora():
    #preparacao
    #print('Iniciando teste de validcao.')

    driver = wb.open_site()
    wb.login('admin@gmail.com','admin',driver)
    wb.cadastrar_locadora(driver)

    #realizar teste

    entrada,saida = wb.preencher_locadora(driver)
    #print('Teste com tuplas verdadeiras.')

    driver.quit()

    assert saida == [], "Saida inesperada"


def test_valid_cliente():
    #preparacao
    #print('Iniciando teste de validcao.')

    driver = wb.open_site()
    wb.login('admin@gmail.com','admin',driver)
    wb.cadastrar_cliente(driver)

    #realizar teste

    entrada,saida = wb.preencher_cliente(driver)
    #print('Teste com tuplas verdadeiras.')

    driver.quit()

    assert saida == [], "Saida inesperada"

def test_valid_locacao():
    #preparacao
    #print('Iniciando teste de validcao.')

    driver = wb.open_site()
    wb.login('admin@gmail.com','admin',driver)
    wb.cadastrar_locacao(driver)

    #realizar teste

    entrada,saida = wb.preencher_locacao(driver)
    #print('Teste com tuplas verdadeiras.')

    driver.quit()

    assert saida == [], "Saida inesperada"
#-------------------------------------------------------------#
def test_invalid_locadora():
    #preparacao
    #print('Iniciando teste de validcao.')

    driver = wb.open_site()
    wb.login('admin@gmail.com','admin',driver)
    wb.cadastrar_locadora(driver)

    #realizar teste

    entrada,saida = wb.preencher_locadora_errado(driver)
    #print('Teste com tuplas verdadeiras.')

    driver.quit()

    assert saida != [], "Saida inesperada"


def test_invalid_cliente():
    #preparacao
    #print('Iniciando teste de validcao.')

    driver = wb.open_site()
    wb.login('admin@gmail.com','admin',driver)
    wb.cadastrar_cliente(driver)

    #realizar teste

    entrada,saida = wb.preencher_cliente_errado(driver)
    #print('Teste com tuplas verdadeiras.')

    driver.quit()

    assert saida != [], "Saida inesperada"

def test_invalid_locacao():
    #preparacao
    #print('Iniciando teste de validcao.')

    driver = wb.open_site()
    wb.login('admin@gmail.com','admin',driver)
    wb.cadastrar_locacao(driver)

    #realizar teste

    entrada,saida = wb.preencher_locacao_errado(driver)
    #print('Teste com tuplas verdadeiras.')

    driver.quit()

    assert saida != [], "Saida inesperada"


