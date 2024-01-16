from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "YOUR_CHROME_DRIVER_PATH"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

element2 = driver.find_element(By.LINK_TEXT, "Contents")
element2.click()

element3 = driver.find_element(By.NAME, "search")
element3.send_keys("Python")
element3.send_keys(Keys.ENTER)