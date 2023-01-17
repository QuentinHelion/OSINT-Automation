import requests
class ApiClient:
    def __init__(self, data):
        self.url = data

    def get(self, data):
        try:
            response = requests.get(self.url, params=data)
        except Exception as e:
            return e

        return response.json()

    def post(self, data):
        try:
            response = requests.post(url, json=data)
        except Exception as e:
            return e
            
        return response.json()
