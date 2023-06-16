from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.com.br/')
driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys("Pote Eletrolux")
driver.implicitly_wait(0.5)
driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
driver.implicitly_wait(6.5)



