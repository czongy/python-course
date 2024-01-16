from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import os
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
GOOGLE_FORM_LINK = os.environ.get("GOOGLE_FORM_LINK")
ZILLOW_LINK = os.environ.get("ZILLOW_LINK")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
res = requests.get(url=ZILLOW_LINK, headers=headers)
res.raise_for_status()
data = res.text

soup = BeautifulSoup(data, "lxml")
addr_card = soup.select("div .property-card-data a")
price_card = soup.select("div .property-card-data span")

addr_list = []
link_list = []
price_list = []

for item in addr_card:
    addr_list.append(item.getText())
    link_list.append(item.attrs.get("href"))
for item in price_card:
    if item.getText()[0] == "$":
        price_list.append(item.getText())

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
driver.get(GOOGLE_FORM_LINK)

for num in range(len(addr_list)):
    qns_one = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    qns_one.click()
    qns_one.send_keys(addr_list[num])
    qns_two = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    qns_two.click()
    qns_two.send_keys(price_list[num])
    qns_three = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    qns_three.click()
    qns_three.send_keys(link_list[num])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    sleep(2)

    if num != len(addr_list):
        driver.find_element(By.LINK_TEXT, "Submit another response").click()
    else:
        break

