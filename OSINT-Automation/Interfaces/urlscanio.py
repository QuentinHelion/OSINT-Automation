import sys
sys.path.append("../")
from Class import ApiClient
from Class import Env

class Urlscanio:
    API_URL = "https://urlscan.io/api/v1/scan/"

    def __init__(self):
        print("Init")
        env = Env("../../.env") # .env reader
        self.api_key = env.get_var("API_KEY_USISCANIO")
        self.apiClient = ApiClient(self.API_URL)

    def scan(self, url):
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
        return self.apiClient.get()
