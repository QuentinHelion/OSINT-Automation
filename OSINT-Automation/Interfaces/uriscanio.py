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
            "Content - Type": "application / json"
        }

        data = {
            "url": url,
            "visibility": "public"
        }

        self.apiClient.post(headers, data)
