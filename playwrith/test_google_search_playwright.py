from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        # Inicia o navegador
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Abre o Google
        page.goto("https://www.google.com")

        # Localiza o campo de busca, insere o termo e pressiona Enter
        page.fill("input[name='q']", "pytest selenium playwright")
        page.press("input[name='q']", "Enter")

        # Aguarda que os resultados carreguem
        page.wait_for_load_state("networkidle")

        # Verifica se o título da página contém o termo de pesquisa
        assert "pytest selenium playwright" in page.title()

        # Fecha o navegador
        browser.close()