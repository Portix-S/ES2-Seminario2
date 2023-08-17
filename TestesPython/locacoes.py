import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://localhost:8080/")


# TESTE CADASTRO DE LOCAÇÃO
def R5():
    print('R5 - TESTE CADASTRO DE LOCAÇÃO')
    print()

    # Encontrar o botão de login usando o seletor CSS
    botao_login = driver.find_element("css selector", 'input[value="Login"]')
    # Clicar no botão de login
    botao_login.click()

    #inserir dados
    #Encontrar o campo de entrada do nome de usuário e inserir o valor
    campo_usuario = driver.find_element("css selector", 'input[name="username"]')
    campo_usuario.send_keys("pietro@pietro.com")

    # Encontrar o campo de entrada da senha e inserir o valor
    campo_senha = driver.find_element("css selector", 'input[name="password"]')
    campo_senha.send_keys("123")

    # Encontrar o botão "Entrar" e clicar nele
    botao_entrar = driver.find_element("css selector", 'input[value="Entrar"]')
    botao_entrar.click()

    #logado como cliente
    # retorna os botoes de navegação
    btns = driver.find_elements('css selector', 'a.nav-link')
    # retorna o botao onde .text == Cadastrar
    btnCadastrar = [btn for btn in btns if btn.text == 'Cadastrar'][0]
    btnCadastrar.click()

    # Na página de cadastro de locacoes
    btnCliente = driver.find_element('id', 'cliente')
    btnCliente.click() # abriu a lista
    btnCliente.find_element('css selector', 'option:nth-child(2)').click() # seleciona a segunda opção (primeira opção é "Selecione")

    btnLocadora = driver.find_element('id', 'locadora')
    btnLocadora.click() # abriu a lista
    btnLocadora.find_element('css selector', 'option:nth-child(2)').click() # seleciona a segunda opção (primeira opção é "Selecione")

    entradaData = driver.find_element('id', 'dataHora')
    # entradaData.send_keys('31/12/2023' + Keys.TAB + '12') # chrome
    entradaData.send_keys('12/31/2023' + Keys.TAB + '12:00' + Keys.TAB + Keys.ARROW_UP) # firefox

    btnSalvar = driver.find_element('css selector', 'button[type="submit"]')
    btnSalvar.click()

    salvou = False
    # confere o url da página atual
    if driver.current_url == 'http://localhost:8080/locacoes/listar':
        salvou = True
        print('Salvou com sucesso!')
    elif driver.current_url == 'http://localhost:8080/locacoes/salvar':
        salvou = False
        print('Não salvou! (provavelmente já existe uma locação com esses dados)')

    if salvou:
        # testa se existe a tabela de locadoras
        tabela = driver.find_element('css selector', 'table')
        print(f'Encontrou a tabela? {"Sim" if tabela != None else "Não"}')
        print(f'É visível? {"Sim" if tabela.is_displayed() else "Não"}')

        # testa se existe a linha da locacao
        linhas = tabela.find_elements('css selector', 'tbody tr')
        print(f'Possui locações? {"Sim" if len(linhas) > 0 else "Não"}')

        linha = [linha for linha in linhas if linha.find_element('css selector', 'td:nth-child(4)').text == '2023-12-31 12:00'][0]
        print(f'Encontrou a linha? {"Sim" if linha != None else "Não"}')
        print(f'É do mesmo usuário? {"Sim" if linha.find_element("css selector", "td:nth-child(2)").text == "446.023.648-61" else "Não"}')

        # testa se existe o botão de excluir
        btnExcluir = linha.find_element('css selector', 'td:nth-child(5) button')
        btnExcluir.click()
        print('Click no botão de excluir')

        # testa se existe o botão de confirmar exclusão
        botao_confirmar = driver.find_element('id', 'ok_confirm')
        print(f'Achou Confirmar? {"Sim" if botao_confirmar != None else "Não"}')
        botao_confirmar.click()
        print('Click no botão de confirmar exclusão')

        time.sleep(0.5)

        # testa se a linha foi excluida
        aviso = driver.find_element('css selector', 'div.alert-success span')
        print(aviso.text)
        print(f'Apareceu a confirmação? {"Sim" if aviso.text == "Locação excluída com sucesso." else "Não"}')
        
        # testa se a linha foi excluida
        tabela = driver.find_element('css selector', 'table')
        linhas = tabela.find_elements('css selector', 'tbody tr')
        linha = [linha for linha in linhas if linha.find_element('css selector', 'td:nth-child(4)').text == '2023-12-31 12:00']
        print(f'Encontrou a linha? {"Não" if len(linha) == 0 else "Sim"}')
    

R5()

print()
print('----------------------------------------------')
print()

driver.quit()
