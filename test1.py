# from selenium import webdriver
# browser = webdriver.Chrome

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
# driver = webdriver.Chrome(options=options, executable_path=r'/usr/local/bin/chromedriver')
driver = webdriver.Chrome(options=options, executable_path=r'/snap/bin/chromium.chromedriver')
driver.get("https://news.ycombinator.com/")
driver.save_screenshot('hn_homepage.png')
driver.quit()
