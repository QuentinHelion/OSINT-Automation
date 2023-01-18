import requests
import json
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

    def post(self, data, headers=None):
        print("ApiClient: post")
        if headers:
            response = requests.post(self.url, json=data, headers=headers)
        else:
            response = requests.post(self.url, json=data)
        return response.json()
