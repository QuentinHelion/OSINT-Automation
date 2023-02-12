from Class import *
from Interfaces import *
import time
import json


def main():
    print("Starting...")

    # app = True
    #
    # while app:
    #     result = mainMenu();
    #     if result == "end":
    #         app = False
        # elif result == "harvester":
            # theHarvesterMenu()


    env = Env("../.env") # .env reader

    # Objects
        #Uriscan
    # uri = Urlscanio()
    # urlscanKEY = env.get_var("API_KEY_USISCANIO")
        #Dnscan
    # dns = "google.com"
    # dnscan = Dnscan(dns)
        #Shodan
    shodan = Appshodan(env.get_var("API_KEY_SHODAN"))
        #theHarvester
    # harvester = TheHarvester("google.com")
    # harvester.run()

    mainMenu(urlscanKEY);


   # result = uri.scan("google.com")
   # print(result)
   # print("Waiting for result...")
   # time.sleep(10)  # Sleep for 10s, needed to wait results charge on api
   # print(uri.getResult(result))

    # dnscan.run()


    # print("SHODAN SEARCH . . .")
    # shodan.shodan_search("apache")
    # print("SHODAN HOST . . .")
    # shodan.shodan_host("94.23.249.172")
    # #shodan.shodan_domain_info("google.com")#needs credits
    # hostnames = ["google.com","bing.com","facebook.com"]
    # shodan.shodan_resolve(hostnames)
    # ips = ["23.233.154.32","74.125.227.230","204.79.197.200"]
    # shodan.shodan_reverse(ips)

    print("ending...")


if __name__ == "__main__":
    main()
