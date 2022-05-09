import requests
import datetime as dt
import smtplib
import time


def is_nearby(my_lat, my_long, iss_lat, iss_long):
    if my_lat - 5 <= iss_lat <= my_lat + 5 and my_long - 5 <= iss_long <= my_long + 5:
        return True
    else:
        return False

def is_dark(current_time, sunrise, sunset):
    if current_time > sunset or current_time < sunrise:
        return True
    else:
        return False


# ISS location
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])


# Sunrise and sunset
my_lat = 1.507351
my_long = -0.127758
format = 0
parameters = {"lat": my_lat, "long": my_long, "formatted": format}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

current_time = dt.datetime.now()
current_hour = current_time.hour
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]


# Send email alert if ISS is nearby and if it is dark
while True:
    if is_nearby(my_lat, my_long, iss_lat, iss_long) and is_dark(current_hour, sunrise_hour, sunset_hour):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="my_email@gmail.com", password="password")
            connection.sendmail(from_addr="my_email@gmail.com", to_addrs="recipient@gmail.com",
                                msg="Subject:ISS Alert")
        time.sleep(900)
    time.sleep(60)
