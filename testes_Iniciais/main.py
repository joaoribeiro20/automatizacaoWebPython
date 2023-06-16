from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/selenium/web/inputs.html')
text = driver.find_element(By.XPATH, "/html/body/form/input[1]").tag_name
driver.implicitly_wait(0.5)
print(text)




