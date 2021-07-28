from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

from data import CODES

import os
from dotenv import load_dotenv
load_dotenv()
GVA_USER = os.getenv('GVA_USER')
GVA_PASSWORD = os.getenv('GVA_PASSWORD')

WEBDRIVER_PATH = r'/snap/bin/chromium.chromedriver'

chrome_options = Options()

# This is to attach to a browser.
# The browser should have been launched like:
# /opt/google/chrome/chrome --remote-debugging-port=9222 --user-data-dir='/tmp/banana'
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(WEBDRIVER_PATH, chrome_options=chrome_options)


action = webdriver.ActionChains(driver)

#driver.get('https://appweb.edu.gva.es/adjudicacio/init.do?lang=es&conv=202107590')

for code in CODES:
    btn_add = driver.find_element_by_xpath("//button[@class='afegir']")
    btn_add.click()
    fld_code = driver.find_element_by_xpath('(//input[@name="centre"])[last()]')
    fld_code.send_keys(code)
    action.move_to_element(fld_code)
    # We need this to trigger the AJAX request
    fld_code.send_keys(Keys.TAB)
