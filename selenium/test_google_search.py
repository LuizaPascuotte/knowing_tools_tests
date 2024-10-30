from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    # Inicializa o navegador
    driver = webdriver.Chrome()

    try:
        # Abre o Google
        driver.get("https://www.google.com")

        # Localiza o campo de busca, insere o termo e pressiona Enter
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("pytest selenium playwright")
        search_box.send_keys(Keys.RETURN)

        # Aguarda que os resultados carreguem
        time.sleep(2)

        # Verifica se o título da página contém o termo de pesquisa
        assert "pytest selenium playwright" in driver.title
    finally:
        # Fecha o navegador
        driver.quit()
