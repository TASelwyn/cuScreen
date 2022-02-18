# Automated cuScreen Covid-19 Questionnaire
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://cuscreen.carleton.ca/")

driver.implicitly_wait(30)

driver.find_element(By.XPATH, '//*[@id="userNameInput"]').send_keys("thomasselwyn")
driver.find_element(By.XPATH, '//*[@id="passwordInput"]').send_keys("xxxxxxxxxxxx")
driver.find_element(By.XPATH, '//*[@id="submitButton"]').click()

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/main/div[3]/div/ul/li[1]').click()
driver.find_element(By.XPATH, '//*[@id="864275f1-9af6-436c-bbf5-a9e9d3478788-noFocus"]/fieldset/label[1]').click()
driver.find_element(By.XPATH, '//*[@id="b648d1ad-95a0-4df3-9ee8-d02b88b9a593-noFocus"]/fieldset/label[1]').click()
driver.find_element(By.XPATH, '//*[@id="4614a181-08fd-4ac7-95d0-42e653fd5edd-noFocus"]/fieldset/label[1]').click()
driver.find_element(By.XPATH, '//*[@id="d380a300-55a8-464c-9106-cff4d1eb0775-noFocus"]/fieldset/label[1]').click()
driver.find_element(By.XPATH, '//*[@id="4cbc713a-b8b2-4ad6-ac4b-3f3ffbbcec8b-noFocus"]/fieldset/label[1]').click()
driver.find_element(By.XPATH, '//*[@id="51df76ae-71ea-4822-8351-37d145c429b3-noFocus"]/fieldset/label[1]').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/main/div/div/div/div/div/button').click()
