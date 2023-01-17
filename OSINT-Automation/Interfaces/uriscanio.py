import sys
sys.path.append("../")
from Class import ApiClient

class Uriscanio:
    API_URL = "https://uriscan.io/scan"

    def __init__(self, api_key):
        self.api_key = api_key
        self.apiClient = ApiClient(self.API_URL)

    def call(self, url):
        headers = {
            "X-Auth": self.api_key
        }

        data = {
            "url": url
        }

        self.apiClient.post(headers, data)