from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver2_win32/chromedriver.exe', options=chrome_options)
driver.get('https://www.anywebsite.com')