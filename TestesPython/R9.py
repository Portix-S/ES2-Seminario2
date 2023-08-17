from selenium import webdriver
import Webdriver_Utils as wb
import time


driver = wb.open_site()
wb.login('admin@gmail.com','admin',driver)


try:
    # Lista de URLs das páginas a serem testadas
    urls = [
        "http://localhost:8080/locadoras/cadastrar",
        "http://localhost:8080/locadoras/listar",
        "http://localhost:8080/clientes/cadastrar",
        "http://localhost:8080/clientes/listar",
        "http://localhost:8080/locacoes/cadastrar",
        "http://localhost:8080/locacoes/listar",

    ]

    for url in urls:
        driver.get(url)

        try:
            wb.login('admin@gmail.com','admin',driver)
        except:
            pass
        
        lang_link = driver.find_element("css selector", 'a[href*="?lang=en"]')
        lang_link.click()
        time.sleep(0.5)
        lang_link = driver.find_element("css selector", 'a[href*="?lang=pt"]')
        lang_link.click()
        time.sleep(0.5)
        lang_link = driver.find_element("css selector", 'a[href*="?lang=en"]')
        lang_link.click()

        # Verificar se a página está agora em inglês
        current_url = driver.current_url
    
except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    # Fechar o navegador
    driver.quit()
