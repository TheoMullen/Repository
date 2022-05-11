import requests
from twilio.rest import Client
import os

api_key = "98fe90a2e11bcb0455aa71ba45702e9a"
lat = 51.507351
lon = 0.127758
exclude = "current,minutely,daily"
api_parameters = {"lat": lat, "lon": lon, "exclude": exclude, "appid": api_key}

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = 'AC28175ccf1b8f8b141c74370eb9b834aa'
auth_token = '4e9135cfae4cba1d0b375baeee988e57'


# Check if rain is due in the next 12 hours
response = requests.get(api_endpoint, params=api_parameters)
response.raise_for_status()
data = response.json()

hourly_data = (data["hourly"])
twelve_hour_data = hourly_data[0:12]
id_list = [hour['weather'][0]['id'] for hour in twelve_hour_data]

rain_due = False

for id in id_list:
    if id < 700:
        rain_due = True


# Send a text alert if rain is due
if rain_due:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It will rain today.",
        from_='+19853165886',
        to='+447788663759'
    )

    print(message.status)