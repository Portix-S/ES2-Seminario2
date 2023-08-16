
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://localhost:8080/")

# Encontrar o botão de login usando o seletor CSS
botao_login = driver.find_element("css selector", 'input[value="Login"]')
# Clicar no botão de login
botao_login.click()

#inserir dados
#Encontrar o campo de entrada do nome de usuário e inserir o valor
campo_usuario = driver.find_element("css selector", 'input[name="username"]')
campo_usuario.send_keys("conserta_bike@gmail.com")

# Encontrar o campo de entrada da senha e inserir o valor
campo_senha = driver.find_element("css selector", 'input[name="password"]')
campo_senha.send_keys("123")

# Encontrar o botão "Entrar" e clicar nele
botao_entrar = driver.find_element("css selector", 'input[value="Entrar"]')
botao_entrar.click()

# Demonstrar funções do CRUD

print("\n\nTESTAR LISTAR LOCACOES\n\n")

# Teste Cadastrar - Locadora
btnLocadora = driver.find_element("css selector", "a[href='/locacoes/listar']")
btnLocadora.click()
print(f'Achou Listar Locacoes ?  {"Sim" if btnLocadora != None else "Não"}')

# Há Tabela locadoras
tabela = driver.find_element('css selector', 'table')
print(f'Encontrou? {"Sim" if tabela != None else "Não"}')
print(f'É visível? {"Sim" if tabela.is_displayed() else "Não"}')