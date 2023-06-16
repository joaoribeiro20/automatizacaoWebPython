from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com.br/Maestria-Robert-Greene/dp/8575429817")
txt = driver.find_element(By.XPATH,'//*[@id="a-autoid-4-announce"]').text
driver.implicitly_wait(2.5)
print(txt)