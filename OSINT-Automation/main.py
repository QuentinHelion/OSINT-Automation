from Class import *
from Interfaces import *

def main():
    # app = create_class()
    # print(app.get("/"))
    # app.url("https://uriscan.io/scan")
    # app.post()

    print("Starting...")

    env = Env("../.env")
    print(env.get_var("API_KEY_USISCANIO"))

    uri = Uriscanio(env.get_var("API_KEY_USISCANIO"))
    result = uri.call("google.com")
    print(result)


if __name__ == "__main__":
    main()
