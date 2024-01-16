from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import time

chrome_driver_path = "YOUR_CHROME_DRIVER_PATH"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_element = driver.find_element(By.ID, "cookie")

store = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrade_list = [upgrade.get_attribute("id") for upgrade in store][0:8:][::-1]
store2 = driver.find_elements(By.CSS_SELECTOR, "#store b")
upgrade_cost = [cost.get_attribute("innerHTML") for cost in store2][0:8:][::-1]
cost_list = []
for cost in upgrade_cost:
    cost_list.append(cost.split("-")[1].strip().split()[1].replace(",", ""))

timeout = time() + 60 * 5
timecheck = time() + 5

while True:
    cookie_element.click()
    if time() > timecheck:
        for i in range(len(cost_list)):
            money_element = int(driver.find_element(By.ID, "money").get_attribute("innerHTML").replace(",", ""))
            if money_element >= int(cost_list[i]):
                driver.find_element(By.ID, upgrade_list[i]).click()
                break
        timecheck += 5
    if time() > timeout:
        count = driver.find_element(By.ID, "cps").get_attribute("innerHTML")
        print(count)
        break
