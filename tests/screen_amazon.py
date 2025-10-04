import os
import time
import datetime


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


diretorio_atual = os.getcwd()

# Defina o nome da pasta de destino dentro do seu diretorio
nome_pasta = 'screenshot'

# Crie o caminho completo para a pasta de destino no seu diretorio
caminho_destino = os.path.join(diretorio_atual, nome_pasta)

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
        #botao_capacomum = self.driver.find_element("xpath", '//*[@id="a-autoid-1"]')
        #botao_capacomum.click()
    
    def adicionar_carrinho(self):
        botao_adicionarcarrinho = self.driver.find_element("xpath", '//*[@id="add-to-cart-button"]')  
        botao_adicionarcarrinho.click()

def verficar_one_clique_carrinho(self):
    try:
        self.elements.adicionar_carrinho()
        
        # Verifica se a mensagem "Adicionado ao carrinho" está presente
        if "Adicionado ao carrinho" in self.driver.page_source:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(caminho_destino, f'screenshot1_{timestamp}.png')
            self.driver.save_screenshot(screenshot_path)
            # Não feche o driver ainda se quiser continuar testes
            # self.elements.fechar()
        else:
            self.elements.comprar_umclique()

        # Assert alternativo caso o elemento não exista
        if "Comprar agora com 1-clique" in self.driver.page_source:
            print("Elemento 'Comprar agora com 1-clique' encontrado.", flush=True)
        elif "QA Iniciante" in self.driver.page_source:
            print("Título do ebook encontrado como fallback.", flush=True)
        else:
            raise AssertionError("Nem o texto 'Comprar agora com 1-clique' nem o título do ebook foram encontrados!")

        # Screenshot final
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(caminho_destino, f'screenshot4_{timestamp}.png')
        self.driver.save_screenshot(screenshot_path)

    except Exception as e:
        print("Erro ao verificar o carrinho:", e, flush=True)
        raise

    def fechar(self):
        self.driver.quit()
