import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import time, sleep

load_dotenv()

PROMISED_DOWN = 500
PROMISED_UP = 300
CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(5)
        start = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start.click()
        sleep(55)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").get_attribute("innerHTML")
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").get_attribute("innerHTML")

    def tweet_at_provider(self, text_to_pro):
        self.driver.get("https://twitter.com/home")
        sleep(2)

        user = self.driver.find_element(By.NAME, "text")
        user.send_keys(TWITTER_EMAIL)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_btn.click()
        sleep(20)

        passw = self.driver.find_element(By.NAME, "password")
        passw.send_keys(TWITTER_PASSWORD)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        login_btn.click()
        sleep(5)

        text_input = self.driver.find_element(By.CLASS_NAME, "DraftEditor-editorContainer")
        text_input.click()
        text_input2 = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        text_input2.send_keys(text_to_pro)
        sleep(2)
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_btn.click()
        sleep(100)


daily_time = time() + 24 * 60 * 60

if time() < daily_time:
    speed_twit = InternetSpeedTwitterBot()
    speed_twit.get_internet_speed()
    tested_down = round(float(speed_twit.down))
    tested_up = round(float(speed_twit.up))
    if tested_down < PROMISED_DOWN and tested_up < PROMISED_UP:
        text_to = f"Hey Internet Provider, why is my internet speed {tested_down}down/{tested_up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        speed_twit.tweet_at_provider(text_to)
    else:
        print("Speed is okay")
