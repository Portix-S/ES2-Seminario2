from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select

driver = Chrome()
driver.get("http://127.0.0.1:8080/")

def logar_cliente():
    # Encontrar o botão de login usando o seletor CSS
    driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]').click()
    #botao_login.click()

    #inserir dados
    #Encontrar o campo de entrada do nome de usuário e inserir o valor
    driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys('pietro@pietro.com')
    #campo_usuario.send_keys("pietro@pietro.com")

    # Encontrar o campo de entrada da senha e inserir o valor
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys('123')
    #campo_senha.send_keys("123")

    # Encontrar o botão "Entrar" e clicar nele
    driver.find_element(By.CSS_SELECTOR, 'input[value="LogIn"]').click()
    #botao_entrar.click()

def listar_locacoes_clientes():
    #Encontrar a listagem de locações do cliente
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/locacoes/listar"]').click()

    table = driver.find_element(By.CSS_SELECTOR, 'table tbody')

    #rows = table.find_elements
    for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
        for cell in row.find_elements(By.CSS_SELECTOR, 'td'):
            print(cell.text)

logar_cliente()
listar_locacoes_clientes()





