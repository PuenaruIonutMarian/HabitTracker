import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "YOUR USER NAME PIXELA"
TOKEN = "YOUR TOKEN"
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
    }


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

#autentification header
headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

data_curenta = today.strftime("%Y%m%d")


pixel_add_endpoit = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_add_config = {
    "date": data_curenta,
    "quantity": input("How many kilometers did you cycle today? "),
}

pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{data_curenta}"
pixel_update_config = {
    "quantity": "8"
    }
response = requests.put(url=pixel_update, json=pixel_update_config, headers=headers)




