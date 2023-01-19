import requests
import json
headers = {'API-Key':'','Content-Type':'application/json'}
data = {"url": "https://urlyouwanttoscan.com/path/", "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
print(response)
print(response.json())