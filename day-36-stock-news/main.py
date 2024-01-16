import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API = os.environ.get("ALPHA_API")
NEWS_API = os.environ.get("NEWS_API")
ACC_SID = os.environ.get("ACC_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
ALPHA_ENDPOINT = os.environ.get("ALPHA_ENDPOINT")
NEWS_API_ENDPOINT = os.environ.get("NEWS_API_ENDPOINT")
FROM_PHONE = os.environ.get("FROM_PHONE")
TO_PHONE = os.environ.get("PHONE")

account_sid = ACC_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API
}
stock_response = requests.get(url=ALPHA_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

ytd_price = float(data_list[0]["4. close"])
day_b4_price = float(data_list[1]["4. close"])
difference = ytd_price - day_b4_price
percent = difference / ytd_price * 100

if difference / day_b4_price * 100 < -1 or difference / day_b4_price * 100 > 1:
    # STEP 2: Use https://newsapi.org
    news_params = {
        "apiKey": NEWS_API,
        "q": COMPANY_NAME,
        "language": "en"
    }
    news_response = requests.get(url=NEWS_API_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    news_list = []
    if len(news_data) <= 3:
        for n in range(len(news_data)):
            news_list.append(news_data[n])
    else:
        for n in range(3):
            news_list.append(news_data[n])

    # newsapi = NewsApiClient(api_key=NEWS_API)
    # all_articles = newsapi.get_everything(
    #     q="Tesla",
    #     qintitle=COMPANY_NAME,
    #     language="en",
    #     sort_by="popularity",
    #     from_param=three_days
    # )

    if difference > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"

    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    for n in range(3):
        msg = f"""\n
{STOCK}: {emoji}{int(percent)}%\n
Headlines: {news_list[n]["title"]}\n
Brief: {news_list[n]["description"]}
"""
        # STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.
        message = client.messages.create(
            body=msg,
            from_=FROM_PHONE,
            to=TO_PHONE
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
