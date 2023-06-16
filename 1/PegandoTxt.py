from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.com.br/')
driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[2]').click()
driver.find_element(By.XPATH, '//*[@id="CardInstance07jsmzp3SWgoayOERej8-Q"]/div[2]/div[22]/a').click()



