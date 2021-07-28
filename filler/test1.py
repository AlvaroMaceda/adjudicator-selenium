from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import os
from dotenv import load_dotenv
load_dotenv()
GVA_USER = os.getenv('GVA_USER')
GVA_PASSWORD = os.getenv('GVA_PASSWORD')

WEBDRIVER_PATH = r'/snap/bin/chromium.chromedriver'

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

# To attach to a browser
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=options, executable_path=WEBDRIVER_PATH)



# Login
driver.get('https://appweb.edu.gva.es/adjudicacio/init.do?lang=es&conv=202107590')
input_user = driver.find_element_by_id('usuari')
input_user.send_keys(GVA_USER)
input_pass = driver.find_element_by_id('contrasenya')
input_pass.send_keys(GVA_PASSWORD)
input_pass.send_keys(Keys.ENTER)
input_pass.submit()


# Continue with request
# btn_continue = input_user = driver.find_element_by_id('btnContinuar')
# btn_continue.click()

# Delete draft
def draft_in_course():
    text = driver.page_source.find("Si no desea presentar este borrador tiene la posibilidad de eliminarlo")
    return text != -1

def delete_current_draft():
    if(draft_in_course()):
        driver.find_element_by_id('borrador_eliminar').click()
        driver.find_element_by_id('alerta_acceptar').click()

delete_current_draft()

# Start request
driver.find_element_by_id('guardarIcontinuar1').click()


l=driver.find_element_by_xpath('//a[@title="Añadir fila"]')
l.click()
# driver.find_element_by_xpath('//button[normalize-space()="Click me!"]').click()

# driver.close()
