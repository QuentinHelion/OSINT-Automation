#from Class import *
from Interfaces import *
import time
import json


def main():
    print("Starting...")

    # Objects
        #Uriscan
    #env = Env("../.env") # .env reader
    #uri = Urlscanio(env.get_var("API_KEY_USISCANIO"))
        #Dnscan
    dns = input("Which domain do you want to scan ?")
    dnscan = Dnscan(dns)
    
   # result = uri.scan("google.com")
   # print(result)
   # print("Waiting for result...")
   # time.sleep(10)  # Sleep for 10s, needed to wait results charge on api
   # print(uri.getResult(result))

    dnscan.run()

    print("ending...")


if __name__ == "__main__":
    main()
