from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8080/")

# retorna o botão, tag <a></a>
btnLocadoras = driver.find_element('css selector', '.nav-item:nth-child(2) > .nav-link')
btnLocadoras.click()

# TESTE LISTAGEM DE LOCADORAS
print('R3 - TESTE LISTAGEM DE LOCADORAS')

# testa se existe a tabela de locadoras
tabela = driver.find_element('css selector', 'table')
print(f'Encontrou? {"Sim" if tabela != None else "Não"}')
print(f'É visível? {"Sim" if tabela.is_displayed() else "Não"}')

tabelaHeaders = tabela.find_element("css selector", "thead > tr").text
print(f'Possui os headers esperados? {"Sim" if tabelaHeaders == "# CNPJ Nome Telefone Email Cidade" else "Não, foram encontrados: " + tabelaHeaders}')

# locCadastradas = tabela.find_elements("css selector", "tbody > tr")
# retorna apenas linhas onde display != none
locCadastradas = tabela.find_elements("css selector", "tbody > tr")
locCadastradas = [loc for loc in locCadastradas if loc.is_displayed()]
print(f'Possui locadoras cadastradas? {"Sim, existem " + str(len(locCadastradas)) if len(locCadastradas) > 0 else "Não"}')

print()
print('----------------------------------------------')
print()

# TESTE LISTAGEM DE LOCADORAS POR CIDADE
print('R4 - TESTE LISTAGEM DE LOCADORAS POR CIDADE')

lista = driver.find_element('css selector', 'select') # retorna o select
lista.click() # abre a lista
cidadeEscolhida = lista.find_element('css selector', 'option:nth-child(2)').text # retorna o texto da segunda opção
lista.find_element('css selector', 'option:nth-child(2)').click() # seleciona a segunda opção

print(f'Cidade escolhida: {cidadeEscolhida}')

# testa se existe a tabela de locadoras
tabela = driver.find_element('css selector', 'table')
print(f'Encontrou? {"Sim" if tabela != None else "Não"}')
print(f'É visível? {"Sim" if tabela.is_displayed() else "Não"}')

# testa se as locadoras listadas são da cidade escolhida
# apenas linhas onde display != none
linhas = tabela.find_elements("css selector", "tbody > tr")
linhas = [linha for linha in linhas if linha.is_displayed()]
print(f'Possui locadoras cadastradas? {"Sim, existem " + str(len(linhas)) if len(linhas) > 0 else "Não"}')
print(f'As locadoras listadas são da cidade escolhida? {"Sim" if all(cidadeEscolhida in loc.find_element("css selector", "td:nth-child(6)").text for loc in linhas) else "Não"}')

driver.quit()
