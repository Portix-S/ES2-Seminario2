from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8080/")

def logar(login, password):
    # Encontrar o botão de login usando o seletor CSS
    driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]').click()

    #Encontrar o campo de entrada do nome de usuário e inserir o valor
    driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(login)

    # Encontrar o campo de entrada da senha e inserir o valor
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)

    # Encontrar o botão "Entrar" e clicar nele
    driver.find_element(By.ID, 'login-submit').click()

def listar_locacoes_locadoras():
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/locacoes/listar"]').click()

    table = driver.find_element(By.CSS_SELECTOR, 'table tbody')
    rows = table.find_elements(By.CSS_SELECTOR, 'tr')

    assert len(rows) > 0,'Tabela vazia!'

    for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
        for cell in row.find_elements(By.CSS_SELECTOR, 'td'):
            print(cell.text)

def deslogar():
    driver.find_element(By.CSS_SELECTOR, 'input[value="Logout"]').click()


print("\n\nTESTAR LISTAR LOCACOES\n\n")

# Teste Cadastrar - Locadora
logar('conserta_bike@gmail.com', '123')
listar_locacoes_locadoras()
deslogar()

driver.quit()
