import os
import time
from PIL import Image
import pytesseract

from selenium import webdriver
from screen_amazon import Elements
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        #self.driver = webdriver.Chrome('C:\Tools\chromedriver.exe')
        self.driver.get("https://www.amazon.com.br/")
        self.driver.maximize_window()
        self.elements = Elements(self.driver)

        # Verificar se o CAPTCHA está presente na página
        self.is_captcha_present()
        
        # Continue com as etapas automatizadas do teste
        # Exemplo: Interagir com os elementos da página usando self.elements
        
    def is_captcha_present(self):
        try:
            # Aguarde a presença do elemento do CAPTCHA na página
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="auth-captcha-image"]')))
            
            # Se o elemento do CAPTCHA for encontrado, resolve-o automaticamente
            self.solve_captcha()
        except:
            # Se o elemento do CAPTCHA não for encontrado, continue com o teste
            pass

    def solve_captcha(self):
        # Aguarde um momento para garantir que o captcha esteja totalmente carregado
        time.sleep(2)
        
        # Captura uma screenshot da área onde o CAPTCHA está
        screenshot_path = "captcha_screenshot.png"
        self.driver.save_screenshot(screenshot_path)
        
        # Abra a imagem do CAPTCHA usando PIL (Pillow)
        captcha_image = Image.open(screenshot_path)
        
        # Use OCR (Reconhecimento Óptico de Caracteres) para extrair o texto do CAPTCHA
        captcha_text = pytesseract.image_to_string(captcha_image)
        
        print("CAPTCHA resolvido:", captcha_text)
        
        # Se desejar, você pode adicionar código aqui para preencher automaticamente o campo de captcha no formulário web.

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
