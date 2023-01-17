import requests
class ApiClient:
    def __init__(self, url):
        self.url = url
        print("Init ApiClient")

    def get(self, data):
        print("ApiClient: get")
        try:
            response = requests.get(self.url, params=data)
        except Exception as e:
            return e

        return response.json()

    def post(self, headers, data):
        print("ApiClient: post")
        try:
            response = requests.post(self.url, headers=headers, json=data)
        except Exception as e:
            return e
            
        return response.json()
