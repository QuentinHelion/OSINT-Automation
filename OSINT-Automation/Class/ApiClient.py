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

    def post(self, data, token, headers=None):
        print("ApiClient: post")

        if headers:
            print("With header")
            try:
                response = requests.post(self.url, headers=headers, data=json.dumps(data))
            except Exception as e:
                return e
        else:
            print("Without header")
            try:
                response = requests.post(self.url, data=json.dumps(data))
            except Exception as e:
                return e

        return response.json()
