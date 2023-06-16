from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/selenium/web/inputs.html')

submit_button = driver.find_element(By.XPATH, '/html/body/form/input[20]')
submit_button.click()

text = driver.find_element(By.XPATH, "/html/body/form/input[1]").tag_name
driver.implicitly_wait(0.5)

print(text)




