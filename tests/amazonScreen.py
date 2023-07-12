from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#mapeamento dos elementos da tela de inicio, pesquisa e tela dos ebooks
class Elements:
    def __init__(self, driver):
        self.driver = driver
    
    def campo_pesquisa(self, texto_pesquisa):
        campo_pesquisa = self.driver.find_element("xpath", '//*[@id="twotabsearchtextbox"]')
        campo_pesquisa.click()
        campo_pesquisa.send_keys(texto_pesquisa)

    def botao_lupa(self):
        botao_lupa = self.driver.find_element("xpath",'//*[@id="nav-search-submit-button"]')
        botao_lupa.click()

    def limpar_texto(self):
        campo_pesquisa = self.driver.find_element("xpath", '//*[@id="twotabsearchtextbox"]')
        campo_pesquisa.clear()

    def qa_iniciante(self):
        botao_qainiciante = self.driver.find_element("xpath", '//*[@data-asin="B0B7GMVYJS"]')
        botao_qainiciante.click()

    def manual_qa(self):
        botao_manualqainiciante = self.driver.find_element("xpath", '//*[@data-asin="B0C2X172QC"]')
        botao_manualqainiciante.click()
        botao_capacomum = self.driver.find_element("xpath", '//*[@id="a-autoid-1"]')
        botao_capacomum.click()
    
    def adicionar_carrinho(self):
        botao_adicionarcarrinho = self.driver.find_element("xpath", '//*[@id="add-to-cart-button"]')
        botao_adicionarcarrinho.click()
        
    def fechar(self):
        self.driver.quit()
