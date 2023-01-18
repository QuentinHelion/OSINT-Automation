from Class import *
from Interfaces import *

def main():
    # app = create_class()
    # print(app.get("/"))
    # app.url("https://uriscan.io/scan")
    # app.post()

    api = ApiClient("http://localhost:5000")
    headers = {
        "Content - Type": "application / json"
    }

    data = {
        "visibility": "public"
    }

    print(api.post(data))
    # print(api.get("hey"))

    # print("Starting...")
    #
    # env = Env("../.env")
    # print(env.get_var("API_KEY_USISCANIO"))
    #
    # uri = Uriscanio(env.get_var("API_KEY_USISCANIO"))
    # result = uri.call("google.com")
    # print(result)

    print("ending...")


if __name__ == "__main__":
    main()
