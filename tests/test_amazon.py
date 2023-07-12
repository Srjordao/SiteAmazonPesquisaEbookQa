import os
import time
from selenium import webdriver
from screen_amazon import Elements
from webdriver_manager.chrome import ChromeDriverManager

diretorio_atual = os.getcwd()

# Defina o nome da pasta de destino
nome_pasta = 'screenshot'

# Crie o caminho completo para a pasta de destino
caminho_destino = os.path.join(diretorio_atual, nome_pasta)

class AmazonTest:
    
    #inicia o navegador
    def __init__(self):
        #self.driver = webdriver.Chrome('C:\Tools\chromedriver.exe')
        #self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Executar em modo headless
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.amazon.com.br/")
        self.driver.maximize_window()
        self.elements = Elements(self.driver)

    #realiza a busca do primeiro ebook e tira print
    def run_test_qainiciante(self):
        self.elements.campo_pesquisa("QA Iniciante: Dicas, conceitos,modelos e opiniões sobre qualidade de software (QAINICIANTE Livro 1)")
        screenshot_path = os.path.join(caminho_destino, 'screenshot1.png')
        self.driver.save_screenshot(screenshot_path)
        self.elements.botao_lupa()
        self.elements.qa_iniciante()
        assert "Onde tudo começa! QA iniciante!"
        screenshot_path = os.path.join(caminho_destino, 'screenshot2.png')
        self.driver.save_screenshot(screenshot_path)
        self.elements.fechar()
        
    #realiza a busca do segundo ebook e tirar print - 2
    def run_test_manualqa(self):
        self.__init__()
        self.elements.campo_pesquisa("Manual do QAINICIANTE: Um Guia para implementar a qualidade de software")
        screenshot_path = os.path.join(caminho_destino, 'screenshot3.png')
        self.driver.save_screenshot(screenshot_path)
        self.elements.botao_lupa()
        time.sleep(2)
        self.elements.manual_qa()
        self.elements.adicionar_carrinho()
        assert "Adicionado ao carrinho"
        screenshot_path = os.path.join(caminho_destino, 'screenshot4.png')
        self.driver.save_screenshot(screenshot_path)
        self.elements.fechar()
       
test = AmazonTest()

# Teste 1: Realiza a busca do ebook QAINICIANTE
test.run_test_qainiciante()

# Teste 2: Realiza a busca do ebook Manual do QAINICIANTE
test.run_test_manualqa()


