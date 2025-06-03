import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
Account_SID = os.getenv("TWILIO_ACCOUNT_SID")
Auth_Token = os.getenv("TWILIO_AUTH_TOKEN")
SENDPHONENUMBER = os.getenv("SEND_PHONE_NUMBER")
RECEIVEPHONENUMBER = os.getenv("RECEIVE_PHONE_NUMBER")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


parameters1 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response = requests.get("https://www.alphavantage.co/query",params = parameters1)
response.raise_for_status()

daily_data = list(response.json()["Time Series (Daily)"].keys())
# print(daily_data[0])
# print(response.json()["Time Series (Daily)"][daily_data[0]])
open_price_curr_day = float(response.json()["Time Series (Daily)"][daily_data[0]]["1. open"])

close_price_prev_day = float(response.json()["Time Series (Daily)"][daily_data[1]]["4. close"])

change_perc = ((open_price_curr_day-close_price_prev_day)/open_price_curr_day)*100

# print(abs(change_perc))



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    parameters2 = {
        "q" : "tesla",
        "from": str(daily_data[0]),
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get("https://newsapi.org/v2/everything",params = parameters2)
    news_response.raise_for_status()
    # print(news_response.json())
    news_data = list(news_response.json()["articles"])
    # print(news_data[0])
    titles = []
    desc = []
    for i in range(0,3):
        titles.append(news_data[i]["title"])
        desc.append(news_data[i]["description"])
    for i in range(0,3):
        titles.append(titles[i])
        desc.append(desc[i])
    return titles,desc     
           
## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number. 
def send_sms(change_perc,titles):
    client = Client(Account_SID,Auth_Token)
    up_msg_creation = f"TSLA 🔺{change_perc}\nHeadline: {titles[0]}"
    down_msg_creation = f"TSLA 🔻{change_perc}\nHeadline: {titles[0]}"
    final_msg = ""
    if(change_perc>0):
        final_msg = up_msg_creation
    else:
        final_msg = down_msg_creation    
    message = client.messages.create(
    body=final_msg,
    from_=SENDPHONENUMBER,
    to=RECEIVEPHONENUMBER,
    )
    print(message.status)


if(abs(change_perc)>=5):
    titles,desc = get_news()
    send_sms(change_perc,titles,desc)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

