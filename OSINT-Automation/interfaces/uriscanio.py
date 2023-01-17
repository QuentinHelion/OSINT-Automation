import requests

api_key = "YOUR_API_KEY"
url = "https://example.com"

headers = {
    "X-Auth": api_key
}

data = {
    "url": url
}

response = requests.post("https://uriscan.io/scan", headers=headers, json=data)

if response.status_code == 200:
    scan_result = response.json()
    print(scan_result)
else:
    print("Error:", response.status_code)
