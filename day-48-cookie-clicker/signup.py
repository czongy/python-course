from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "YOUR_CHROME_DRIVER_PATH"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, 'fName')
lName = driver.find_element(By.NAME, 'lName')
email_addr = driver.find_element(By.NAME, 'email')
btn = driver.find_element(By.TAG_NAME, "button")

fName.send_keys("Jack")
lName.send_keys("Long")
email_addr.send_keys("email@email.com")
btn.send_keys(Keys.ENTER)
time.sleep(5)
