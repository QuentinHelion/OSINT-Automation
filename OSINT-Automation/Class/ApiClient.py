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
            print("With header")
            response = requests.post(self.url, data=json.dumps(data), headers=headers)
        else:
            print("Without header")
            response = requests.post(self.url, data=json.dumps(data))

        return response.json()
