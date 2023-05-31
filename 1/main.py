from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baudaeletronica.com.br/?gclid=EAIaIQobChMIgaTqs8Gf_wIVlirUAR0KJQz2EAAYASAAEgKD0_D_BwE')
driver.implicitly_wait(0.5)
title = driver.title
print(title)