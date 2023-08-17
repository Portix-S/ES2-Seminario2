from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8080/")

def logar_cliente(login, password):
    # Encontrar o botão de login usando o seletor CSS
    driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]').click()
    #botao_login.click()

    #inserir dados
    #Encontrar o campo de entrada do nome de usuário e inserir o valor
    driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(login)
    #campo_usuario.send_keys("pietro@pietro.com")

    # Encontrar o campo de entrada da senha e inserir o valor
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)
    #campo_senha.send_keys("123")

    # Encontrar o botão "Entrar" e clicar nele
    driver.find_element(By.ID, 'login-submit').click()
    #botao_entrar.click()

def assert_cadastro_locacao():
    driver.find_element(By.CSS_SELECTOR, 'a[href*="locacoes/cadastrar"]').click()

    btnCliente = driver.find_element('id', 'cliente')
    btnCliente.click()
    btnCliente.find_element(By.CSS_SELECTOR, 'option:nth-child(2)').click()

    btnLocadora = driver.find_element('id', 'locadora')
    btnLocadora.click() # abriu a lista
    btnLocadora.find_element(By.CSS_SELECTOR, 'option:nth-child(2)').click()

    driver.find_element('id', 'dataHora').send_keys('20/08/2023' + Keys.TAB + '14:00')
    driver.find_element('css selector', 'button[type="submit"]').click()

def deslogar():
    driver.find_element(By.CSS_SELECTOR, 'input[value=Logout]').click()

print('Cadastrando Locação com o Pietro')
logar_cliente('pietro@pietro.com', '123')
assert_cadastro_locacao()
deslogar()

print('Cadastrando Locação com o Rafael')
logar_cliente('rafael@rafael.com', '123')
assert_cadastro_locacao()
deslogar()

driver.quit()
