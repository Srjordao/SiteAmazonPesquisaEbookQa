import os
import time
import pytesseract
import cv2
import requests

from selenium import webdriver
from screen_amazon import Elements
from selenium.webdriver.chrome.options import Options

class AmazonTest:
    
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_driver_dir = os.path.abspath("chromedriverr/chromedriver")
        os.environ["PATH"] += os.pathsep + chrome_driver_dir
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.amazon.com.br/")
        self.driver.maximize_window()
        self.elements = Elements(self.driver)

        captcha_present = self.is_captcha_present()
        
        if captcha_present:
            captcha_text = self.solve_captcha()
            print("CAPTCHA resolvido:", captcha_text)
        
    def is_captcha_present(self):
        try:
            captcha_element = self.driver.find_element_by_xpath('//*[@id="auth-captcha-image"]')
            return True
        except:
            return False

    def solve_captcha(self):
        screenshot_path = "captcha_screenshot.png"
        self.driver.save_screenshot(screenshot_path)
        
        captcha_image = cv2.imread(screenshot_path)
        captcha_text = self.solve_captcha_with_2captcha(captcha_image)  # Utilize a função para resolver o captcha
        
        return captcha_text

    def solve_captcha_with_2captcha(self, captcha_image):
        # Envie a imagem do captcha para o serviço 2captcha
        with open("captcha_screenshot.png", "rb") as f:
            response = requests.post(
                "http://2captcha.com/in.php",
                files={"file": ("captcha_screenshot.png", f)},
                data={"key": "598c95c739f268a552b5a5d26e8a96ba", "method": "base64"}
            )
        captcha_id = response.json()["request"]
        
        # Aguarde até que o captcha seja resolvido
        while True:
            time.sleep(5)
            response = requests.get(
                "http://2captcha.com/res.php",
                params={"key": "SUA_CHAVE_API_2CAPTCHA", "action": "get", "id": captcha_id}
            )
            if "OK" in response.text:
                captcha_text = response.text.split("|")[1]
                return captcha_text

    def test_qainiciante(self):
        self.elements.campo_pesquisa("QA Iniciante: Dicas, conceitos,modelos e opiniões sobre qualidade de software (QAINICIANTE Livro 1)")
        self.driver.save_screenshot("screenshot1.png")
        self.elements.botao_lupa()
        self.elements.qa_iniciante()
        assert "Onde tudo começa! QA iniciante!"
        self.driver.save_screenshot("screenshot2.png")
        self.elements.fechar()
        
    def test_manualqa(self):
        self.__init__()
        self.elements.campo_pesquisa("Manual do QAINICIANTE: Um Guia para implementar a qualidade de software")
        self.driver.save_screenshot("screenshot3.png")
        self.elements.botao_lupa()
        time.sleep(2)
        self.elements.manual_qa()
        self.elements.verficar_one_clique_carrinho()

test = AmazonTest()
test.test_qainiciante()
test.test_manualqa()
