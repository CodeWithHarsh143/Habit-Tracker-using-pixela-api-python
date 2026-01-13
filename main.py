import os
from dotenv import load_dotenv
import requests
import datetime as dt

load_dotenv()

TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")
pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}


#response = requests.post(url=pixela_endpoint,json=parameters) for creating user
#print(response.text)

graph_end_point = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Codeforces and Leetcode Progress",
    "unit":"problems",
    "type":"int",
    "color":"shibafu"
}

header = {
    "X-USER-TOKEN":TOKEN,
}


#response = requests.post(url=graph_end_point,json=graph_config,headers=header) create pixel graph

#print(response.text)

# post data into graph

pixel_data_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.datetime.now()

data_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"1",
}

response = requests.post(url=pixel_data_endpoint,json=data_config,headers=header)
print(response.text)

# for updating data ( if i want  to update todays data) we are using put request
'''
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_data_config = {
    "quantity":"4",
}

response = requests.put(url=update_endpoint,json=update_data_config,headers=header)

print(response.text)

'''

# for deleting specific date pixel
'''
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint,headers=header)

print(response.text)

'''