
import os
import time
import pytesseract
import cv2


from selenium import webdriver
from screen_amazon import Elements
from selenium.webdriver.chrome.options import Options

diretorio_atual = os.getcwd()

# Defina o nome da pasta de destino
nome_pasta = 'screenshot'

# Crie o caminho completo para a pasta de destino
caminho_destino = os.path.join(diretorio_atual, nome_pasta)

class AmazonTest:
    
    # inicia o navegador
    def __init__(self):
        import os  # Adicione esta linha

        #caminho usado para rodar a pipeline no GIT ACTIONS
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Opcional: execute em modo headless
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_driver_dir = os.path.abspath("chromedriverr/chromedriver")  # Atualize o diretório onde o executável do ChromeDriver está localizado
        os.environ["PATH"] += os.pathsep + chrome_driver_dir
        self.driver = webdriver.Chrome(options=chrome_options)

        #caminho usado para rodar local
        self.driver = webdriver.Chrome('C:\Tools\chromedriver.exe')
        self.driver.get("https://www.amazon.com.br/")
        self.driver.maximize_window()
        self.elements = Elements(self.driver)

        # Verificar se o CAPTCHA está presente na página
        captcha_present = self.is_captcha_present()
        
        if captcha_present:
            # Resolver o CAPTCHA automaticamente
            captcha_text = self.solve_captcha()
            print("CAPTCHA resolvido:", captcha_text)
        
        # Continue com as etapas automatizadas do teste
        # Exemplo: Interagir com os elementos da página usando self.elements
        
    def is_captcha_present(self):
        try:
            # Tenta localizar o elemento do CAPTCHA na página
            captcha_element = self.driver.find_element_by_xpath('//*[@id="auth-captcha-image"]')
            return True
        except:
            # Se o elemento do CAPTCHA não for encontrado, retorna False
            return False

    def solve_captcha(self):
        # Captura uma screenshot da área onde o CAPTCHA está
        screenshot_path = "captcha_screenshot.png"
        self.driver.save_screenshot(screenshot_path)
        
        # Carrega a imagem do CAPTCHA
        captcha_image = cv2.imread(screenshot_path)
        
        # Usa OCR (Reconhecimento Óptico de Caracteres) para extrair o texto do CAPTCHA
        captcha_text = pytesseract.image_to_string(captcha_image)
        
        return captcha_text


    # realiza a busca do primeiro ebook e tira print
    def test_qainiciante(self):
        self.elements.campo_pesquisa("QA Iniciante: Dicas, conceitos,modelos e opiniões sobre qualidade de software (QAINICIANTE Livro 1)")
        os.makedirs(caminho_destino, exist_ok=True)
        screenshot_path = os.path.join(caminho_destino, 'screenshot1.png')
        self.driver.save_screenshot(screenshot_path)
        self.elements.botao_lupa()
        self.elements.qa_iniciante()
        assert "Onde tudo começa! QA iniciante!"
        screenshot_path = os.path.join(caminho_destino, 'screenshot2.png')
        self.driver.save_screenshot(screenshot_path)
        self.elements.fechar()
        
    # realiza a busca do segundo ebook e tirar print - 2
    def test_manualqa(self):
        self.__init__()
        self.elements.campo_pesquisa("Manual do QAINICIANTE: Um Guia para implementar a qualidade de software")
        os.makedirs(caminho_destino, exist_ok=True)
        screenshot_path = os.path.join(caminho_destino, 'screenshot3.png')
        self.driver.save_screenshot(screenshot_path)
        self.elements.botao_lupa()
        time.sleep(2)
        self.elements.manual_qa()
        self.elements.verficar_one_clique_carrinho


test = AmazonTest()

# Teste 1: Realiza a busca do ebook QAINICIANTE
test.test_qainiciante()

# Teste 2: Realiza a busca do ebook Manual do QAINICIANTE
test.test_manualqa()

