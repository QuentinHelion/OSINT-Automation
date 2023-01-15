import requests
class ApiClient:
    def __init__(self, data):
        self.url = data

    def get(self, data):
        response = requests.get(self.url, params=data)
        return response.json()

    def post(self, data):
        response = requests.post(url, json=data)
        return response.json()
