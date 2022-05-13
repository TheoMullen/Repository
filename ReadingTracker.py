import requests
import datetime as dt

USERNAME = "my_username"
TOKEN = "my_token"
GRAPH_ID = "graph"



#Make a Pixela account

pixella_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixella_endpoint, json=parameters)
# print(response.text)



#Set up a graph online

graph_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Reading Tracker",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)



#Functions to change the graph data

def post_today(quantity):
    day = dt.datetime.today()
    date = day.strftime("%Y%m%d")

    pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
    pixel_parameters = {
        "date": date,
        "quantity": "1"
    }

    response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
    print(response.text)

    
def update(quantity, day, month, year):
    day = dt.datetime(day=day, month=month, year=year)
    date = day.strftime("%Y%m%d")

    update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date}"
    update_parameters = {
        "quantity": str(quantity)
    }

    response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
    print(response.text)


def delete(day, month, year):
    day = dt.datetime(day=day, month=month, year=year)
    date = day.strftime("%Y%m%d")

    delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{date}"

    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

