import requests
from twilio.rest import Client
from datetime import date, timedelta


STOCK = "TSLA"
NAME = "Tesla"



# Find any significant daily changes in the stock's value

date = date.today()
yesterday_date = str(date - timedelta(days=1))

full_stock_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
stock_url = "https://www.alphavantage.co/query"
stock_api_key = "MBRJN26V4VYUWAOH"
stock_api_parameters = {"function": "TIME_SERIES_DAILY", "symbol": STOCK, "apikey": stock_api_key}
response = requests.get(stock_url, params=stock_api_parameters)
response.raise_for_status()
data = response.json()

daily_data = data["Time Series (Daily)"]
date_list = list(daily_data.keys())

send_alert = False

if yesterday_date in date_list:
    yesterday_price = float(daily_data[yesterday_date]['4. close'])
    previous_date = date_list[1]
    previous_price = float(daily_data[previous_date]['4. close'])
    change = ((yesterday_price-previous_price)/previous_price) * 100

    if change > 5:
        movement = f"🔺{round(change, 2)}%"
        send_alert = True
    if change < -5:
        movement = f"🔻{round(change, 2)}%"
        send_alert = True



# Prepare an alert with relevant news articles

full_news_url = "https://newsapi.org/v2/everything?q=tesla&from=2022-04-12&sortBy=publishedAt&apiKey=API_KEY"
news_url = "https://newsapi.org/v2/everything"
new_api_key = "b5ca3485a8ab4c20a8fa000a0f4b141c"
news_api_parameters = {"q": NAME, "from": date_list[1], "sortBy": "relevancy", "language": "en", "apiKey": new_api_key}
news_response = requests.get(url=news_url, params=news_api_parameters)
news_response.raise_for_status()
news_data = news_response.json()


alert = f"""
TSLA: {movement} 

Headline: {news_data['articles'][0]["title"]} 
Description: {news_data['articles'][0]["description"]} 

Headline: {news_data['articles'][1]["title"]} 
Description: {news_data['articles'][1]["description"]} 

Headline: {news_data['articles'][2]["title"]} 
Description: {news_data['articles'][2]["description"]}
"""



# Send a text alert via Twilio

if send_alert:
    client = Client(sid, auth_token)
    message = client.messages.create(body=alert, from_=send_number, to=my_number)

    print(message.status)
