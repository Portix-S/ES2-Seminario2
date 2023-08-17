
from selenium import webdriver

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

print("\n\nTESTAR CADASTRAR LOCADORA\n\n")

# Teste Cadastrar - Locadora
btnLocadora = driver.find_element("css selector", "a[href='/locadoras/cadastrar']")
btnLocadora.click()
print(f'Achou Cadastra Cliente? {"Sim" if btnLocadora != None else "Não"}')

# Nome
campo_nome = driver.find_element("css selector", 'input[name="nome"]')
campo_nome.send_keys("Locadora Teste")
print(f'Achou Nome? {"Sim" if campo_nome!= None else "Não"}')

# Cidade
campo_cidade = driver.find_element("css selector", 'input[name="cidade"]')
campo_cidade.send_keys("Ribeirão Preto")
print(f'Achou Cidade? {"Sim" if campo_cidade != None else "Não"}')

# Telefone

campo_telefone = driver.find_element("css selector", 'input[name="telefone"]')
campo_telefone.send_keys("1499998888")
print(f'Achou Telefone? {"Sim" if campo_telefone != None else "Não"}')

# Email
campo_email = driver.find_element("css selector", 'input[name="email"]')
campo_email.send_keys("torenzo@gmail.com")
print(f'Achou Email? {"Sim" if campo_email != None else "Não"}')

# CNPJ
campo_cnpj = driver.find_element("css selector", 'input[name="CNPJ"]')
campo_cnpj.send_keys("12341238910111")
print(f'Achou CPF? {"Sim" if campo_cnpj != None else "Não"}')

# Senha
campo_senhaloc = driver.find_element("css selector", 'input[name="senha"]')
campo_senhaloc.send_keys("123")
print(f'Achou Senha? {"Sim" if campo_senhaloc != None else "Não"}')

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
botao_editar = driver.find_element("css selector", "a[href='/locadoras/editar/8']")
botao_editar.click()
print(f'Achou Editar? {"Sim" if botao_editar != None else "Não"}')

# Trocar apenas alguns dos aspectos

# Nome
campo_nome = driver.find_element("css selector", 'input[name="nome"]')
campo_nome.clear()
campo_nome.send_keys("Locadora Torenzo")
print(f'Achou Para Editar Nome? {"Sim" if campo_nome!= None else "Não"}')

# Cidade
campo_cidade = driver.find_element("css selector", 'input[name="cidade"]')
campo_cidade.clear()
campo_cidade.send_keys("São Paulo")
print(f'Achou Para Editar Cidade? {"Sim" if campo_cidade != None else "Não"}')

# Telefone

campo_telefone = driver.find_element("css selector", 'input[name="telefone"]')
campo_telefone.clear()
campo_telefone.send_keys("1699118888")
print(f'Achou Para Editar Telefone? {"Sim" if campo_telefone != None else "Não"}')

# Email
campo_email = driver.find_element("css selector", 'input[name="email"]')
campo_email.clear()
campo_email.send_keys("careca@gmail.com")
print(f'Achou Para Editar Email? {"Sim" if campo_email != None else "Não"}')

# Senha
campo_senhaloc = driver.find_element("css selector", 'input[name="senha"]')
campo_senhaloc.send_keys("123")
print(f'Achou Senha? {"Sim" if campo_senhaloc != None else "Não"}')


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
botao_remover = driver.find_element("id", "btn_locadoras/excluirPorId/8")
botao_remover.click()
print(f'Achou Remover? {"Sim" if botao_remover != None else "Não"}')

botao_confirmar = driver.find_element("id", 'ok_confirm')
botao_confirmar.click()
print(f'Achou Confirmar? {"Sim" if botao_confirmar != None else "Não"}')

driver.quit()
