from Class import *
from Interfaces import *
import json


def main():
    # app = create_class()
    # print(app.get("/"))
    # app.url("https://uriscan.io/scan")
    # app.post()

    # api = ApiClient("https://urlscan.io/api/v1/scan/")
    # headers = {
    #     "API-Key": "845e7986-30af-4ea3-b7b1-5111a4e8046d",
    #     "Content - Type": "application / json"
    # }
    #
    # data = {
    #     "url": "https://urlyouwanttoscan.com/path/",
    #     "visibility": "public"
    # }
    #
    # api.post(data, headers)
    # print(api.get("hey"))

    print("Starting...")

    env = Env("../.env")
    # print(env.get_var("API_KEY_USISCANIO"))

    uri = Uriscanio(env.get_var("API_KEY_USISCANIO"))
    result = uri.call("google.com")
    print(result)

    print("ending...")


if __name__ == "__main__":
    main()
