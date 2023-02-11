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
        #Shodan
    shodan = Appshodan("API_KEY_SHODAN")
    
   # result = uri.scan("google.com")
   # print(result)
   # print("Waiting for result...")
   # time.sleep(10)  # Sleep for 10s, needed to wait results charge on api
   # print(uri.getResult(result))

    dnscan.run()

    #harvester = TheHarvester("google.com")
    #harvester.run()
    
    print("SHODAN SEARCH . . .")
    shodan.shodan_search("apache")
    print("SHODAN HOST . . .")
    shodan.shodan_host("94.23.249.172")
    #shodan.shodan_domain_info("google.com")#needs credits
    hostnames = ["google.com","bing.com","facebook.com"]
    shodan.shodan_resolve(hostnames)
    ips = ["23.233.154.32","74.125.227.230","204.79.197.200"]
    shodan.shodan_reverse(ips)

    print("ending...")


if __name__ == "__main__":
    main()
