import sys
sys.path.append("../")
from Class import ApiClient

class Uriscanio:
    API_URL = "https://urlscan.io/api/v1/scan/"

    def __init__(self, api_key):
        print("Init")
        self.api_key = api_key
        self.apiClient = ApiClient(self.API_URL)

    def call(self, url):
        headers = {
            "API-Key": self.api_key,
            "Content-Type": "application/json"
        }

        data = {
            "url": url,
            "visibility": "public"
        }
        print(data)

        return self.apiClient.post(data, headers)

    def getResult(self, response):
        self.apiClient.url = response["api"]
        print(self.apiClient.url)

        return self.apiClient.get()
