# todo: create requirements file
# todo: find browser automation libraries
# todo: download excel file with list of goods

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# brauzer va unga bolgan adresni korsatamiz
service = Service(executable_path="D:\\GitHubRepos\\automate_smartup\\chromedriver.exe")
options = selenium.webdriver.ChromeOptions()
driver = selenium.webdriver.Chrome(service=service, options=options)

driver.get('https://www.saucedemo.com/')