
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
campo_usuario.send_keys("admin@gmail.com")

# Encontrar o campo de entrada da senha e inserir o valor
campo_senha = driver.find_element("css selector", 'input[name="password"]')
campo_senha.send_keys("admin")

# Encontrar o botão "Entrar" e clicar nele
botao_entrar = driver.find_element("css selector", 'input[value="Entrar"]')
botao_entrar.click()

# Demonstrar funções do CRUD

print("\n\nTESTAR CADASTRAR CLIENTE\n\n")

# Teste Cadastrar - Cliente
btnCliente = driver.find_element('css selector', '.nav-item:nth-child(2) > .nav-link')
btnCliente.click()
print(f'Achou Cadastra Cliente? {"Sim" if btnCliente != None else "Não"}')

# Nome
campo_nome = driver.find_element("css selector", 'input[name="nome"]')
campo_nome.send_keys("Cliente Teste")
print(f'Achou Nome? {"Sim" if campo_nome!= None else "Não"}')

# CPF
campo_cnpj = driver.find_element("css selector", 'input[name="CPF"]')
campo_cnpj.send_keys("12345678910111")
print(f'Achou CPF? {"Sim" if campo_cnpj != None else "Não"}')

# Sexo

gender_select = Select(driver.find_element("id", "sexo"))
gender_select.select_by_visible_text("Masculino")
print(f'Achou Sexo? {"Sim" if gender_select != None else "Não"}')

# Data de Nascimento
campo_data = driver.find_element("css selector", 'input[name="dataNascimento"]')
campo_data.send_keys("2023-08-16") # AAAA-MM-DD
print(f'Achou Data de Nascimento? {"Sim" if campo_data != None else "Não"}')

# Telefone

campo_telefone = driver.find_element("css selector", 'input[name="telefone"]')
campo_telefone.send_keys("1111111-1111")
print(f'Achou Telefone? {"Sim" if campo_telefone != None else "Não"}')

# Email
campo_email = driver.find_element("css selector", 'input[name="email"]')
campo_email.send_keys("testegrats@gmail.com")
print(f'Achou Email? {"Sim" if campo_email != None else "Não"}')

# Senha
campo_senhaloc = driver.find_element("css selector", 'input[name="senha"]')
campo_senhaloc.send_keys("123")
print(f'Achou Senha? {"Sim" if campo_senhaloc != None else "Não"}')

# Papel
papel_select = Select(driver.find_element("id", "papel"))
papel_select.select_by_visible_text("Cliente")
print(f'Achou Papel {"Sim" if papel_select != None else "Não"}')

# Salvar
botao_salvar = driver.find_element("css selector", 'button[type="submit"]')
botao_salvar.click()

# Teste Listagem de Clientes
print("\n\nTESTAR EDITAR CLIENTE\n\n")

# Lista
tabela = driver.find_element('css selector', 'table')
print(f'Encontrou? {"Sim" if tabela != None else "Não"}')
print(f'É visível? {"Sim" if tabela.is_displayed() else "Não"}')

# Editar
botao_editar = driver.find_element("css selector", "a[href='/clientes/editar/21']")
botao_editar.click()
print(f'Achou Editar? {"Sim" if botao_editar != None else "Não"}')

# Trocar apenas alguns dos aspectos

# Nome
campo_nome = driver.find_element("css selector", 'input[name="nome"]')
campo_nome.clear()
campo_nome.send_keys("Rafaela")
print(f'Achou Editar Nome? {"Sim" if campo_nome!= None else "Não"}')

# Sexo
gender_select = Select(driver.find_element("id", "sexo"))
gender_select.select_by_visible_text("Feminino")
print(f'Achou Sexo? {"Sim" if gender_select != None else "Não"}')

# Data de Nascimento
campo_data = driver.find_element("css selector", 'input[name="dataNascimento"]')
campo_data.clear()
campo_data.send_keys("2023-08-15") # AAAA-MM-DD
print(f'Achou Editar Data de Nascimento? {"Sim" if campo_data != None else "Não"}')

# Telefone

campo_telefone = driver.find_element("css selector", 'input[name="telefone"]')
campo_telefone.clear()
campo_telefone.send_keys("11111111112")
print(f'Achou Telefone? {"Sim" if campo_telefone != None else "Não"}')

# Email
campo_email = driver.find_element("css selector", 'input[name="email"]')
campo_email.clear()
campo_email.send_keys("grats@gmail.com")
print(f'Achou Email? {"Sim" if campo_email != None else "Não"}')

# Senha
campo_senhaloc = driver.find_element("css selector", 'input[name="senha"]')
campo_senhaloc.send_keys("123")
print(f'Achou Senha? {"Sim" if campo_senhaloc != None else "Não"}')

# Papel
papel_select = Select(driver.find_element("id", "papel"))
papel_select.select_by_visible_text("Admin")
print(f'Achou Papel {"Sim" if papel_select != None else "Não"}')

# Salvar
botao_salvar = driver.find_element("css selector", 'button[type="submit"]')
botao_salvar.click()
print(f'Achou Salvar? {"Sim" if botao_salvar != None else "Não"}')

# Remover cliente

# Lista
tabela = driver.find_element('css selector', 'table')
print(f'Encontrou? {"Sim" if tabela != None else "Não"}')
print(f'É visível? {"Sim" if tabela.is_displayed() else "Não"}')

print("\n\nTESTAR REMOVER CLIENTE\n\n")
botao_remover = driver.find_element("id", "btn_clientes/excluirPorId/21")
botao_remover.click()
print(f'Achou Remover? {"Sim" if botao_remover != None else "Não"}')

botao_confirmar = driver.find_element("id", 'ok_confirm')
botao_confirmar.click()
print(f'Achou Confirmar? {"Sim" if botao_confirmar != None else "Não"}')