from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#opens google then searches for bowiestate.edu
driver.get("https://google.com")
search = driver.find_element(By.NAME, 'q')
search.send_keys('bowiestate.edu')
search.send_keys(Keys.RETURN)
time.sleep(1)

#clickks on first result
first_result = driver.find_element(By.CSS_SELECTOR,'h3')
first_result.click()
time.sleep(1)

mybsu = driver.find_element(By.LINK_TEXT, 'MyBSU')
mybsu.click()
time.sleep(1)


time.sleep(10)

driver.quit()