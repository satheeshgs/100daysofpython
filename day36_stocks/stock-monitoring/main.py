import os
from dotenv import load_dotenv
import requests
import datetime
from twilio.rest import Client

load_dotenv()

def get_news(ENDPOINT, APIKEY, NAME):
    parameters = {
        "apiKey": APIKEY,
        "q": NAME,
        "language": "en"
    }

    response = requests.get(url=ENDPOINT, params=parameters)
    return response.json()


#configurations
STOCK_ENDPOINT = os.getenv('STOCK_ENDPOINT')
NEWS_ENDPOINT = os.getenv('NEWS_ENDPOINT')

API_KEY_STOCKS = os.getenv('API_KEY_STOCKS')
API_KEY_NEWS = os.getenv('API_KEY_NEWS')
#Twilio credentials
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN_TWILIO = os.getenv('AUTH_TOKEN')

STOCK = os.getenv('STOCK')
COMPANY_NAME = os.getenv('COMPANY_NAME')

#yesterday and day before
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = today - datetime.timedelta(days=2)

# print(yesterday, day_before_yesterday)

#Get stock data
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": API_KEY_STOCKS
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()
# print(stock_data)
yesterday_close_price = float(stock_data['Time Series (Daily)'][str(yesterday)]['4. close'])
day_before_close_price = float(stock_data['Time Series (Daily)'][str(day_before_yesterday)]['4. close'])

# print(yesterday_close_price, day_before_close_price)

#calculate percentage increase/ decrease
percent_change = round(abs(yesterday_close_price-day_before_close_price)/day_before_close_price*100, 2)

#Symbol for percentage change
if yesterday_close_price > day_before_close_price:
    price_change = '🔺'
else:
    price_change = '🔻'

# print(f"Percent change: {percent_change}")
if percent_change > 5:
    news_data = get_news(NEWS_ENDPOINT, API_KEY_NEWS, COMPANY_NAME)
    company_news = news_data['articles'][slice(3)]

    # twilio client setup
    client = Client(ACCOUNT_SID, AUTH_TOKEN_TWILIO)

    for news in company_news:
        # print(f'{news["title"]}: {news["description"]}')
        message = client.messages.create(
            from_='+15802327032',
            body=f'{STOCK}: {price_change} {percent_change}%\n\n'
                 f'Headline: {news["title"]}\n\n'
                 f'Brief: {news["description"]}',
            to='+14372141643'
        )


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.





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

