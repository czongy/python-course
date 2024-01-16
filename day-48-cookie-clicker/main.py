from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "YOUR_CHROME_DRIVER_PATH"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

driver.get("https://www.python.org/")
# ele = driver.find_element(By.CLASS_NAME, "a-offscreen")
# ele = driver.find_element(By.CSS_SELECTOR, ".a-price span")
# ele = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# price = ele.get_attribute('innerHTML')

# ele = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li")
ele = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li")
event_list = {}
for num in range(len(ele)):
    event_list[num] = {
        "date": ele[num].text[:5],
        "name": ele[num].text[6:]
    }

print(event_list)

driver.quit()