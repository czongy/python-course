import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']

URL = "https://www.amazon.sg/AMD-Ryzen-5700X-16-Thread-Processor/dp/B09VCHQHZ6?ref_=Oct_DLandingS_D_3af753e7_60"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
           "Accept-Language": "en-US,en;q=0.9"}
response = requests.get(URL, headers=HEADERS)
amazon_web = response.text

soup = BeautifulSoup(amazon_web, "lxml")
price = soup.find(class_="a-offscreen").getText().strip("S$")

if float(price) < 300:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=USER, password=PASSWORD)
    connection.sendmail(from_addr=USER, to_addrs=USER,
                        msg=f"Subject:Buy Now\n\nPrice is below $200.\n{URL}")
