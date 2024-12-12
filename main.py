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
search.send_keys('Bowie State University')
search.send_keys(Keys.RETURN)
time.sleep(1)

#clickks on first result
first_result = driver.find_element(By.CSS_SELECTOR,'h3')
first_result.click()
time.sleep(1)

#clicks on my bsu through
mybsu = driver.find_element(By.LINK_TEXT, 'MyBSU')
mybsu.click()
time.sleep(2)

#clicks on blackboard through css
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)
blackboard = driver.find_element(By.LINK_TEXT, 'Blackboard')
blackboard.click()
time.sleep(2)

# Locate the first textbox
first_textbox = driver.find_element(By.CSS_SELECTOR, "input[type='text']") 

# Click the textbox
first_textbox.click()

# Optionally, send keys to the textbox
first_textbox.send_keys("salimh0807")

time.sleep(3)

first_textbox.send_keys(Keys.ENTER)

# Locate the second textbox
second_textbox = driver.find_element(By.CSS_SELECTOR, "input[type='text']") 

# Click the textbox
second_textbox.click()

#send keys to the textbox
second_textbox.send_keys("jjjhhjhj")
time.sleep(15)

time.sleep(10)

driver.quit()