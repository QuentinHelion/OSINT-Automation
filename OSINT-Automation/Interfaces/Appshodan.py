import shodan
import os
import json
from Class import ApiClient
from Class import Env

#initialise the shodan API object

    #for CLI :
    #shodan init <API_KEY>

class Appshodan:

    def __init__(self):
        #set key
        env = Env("../../.env") # .env reader
        self.api_key = env.get_var("API_KEY_SHODAN")
        self.api = shodan.Shodan(self.api_key) #will be used by shodan methods


    def write_to_file_json(self, query, output_list):
        PATH_TO_RESULTS = "Results/Shodan/"
        self.query = query
        self.output_list = output_list

        filename = query + '.json'
        output_file = PATH_TO_RESULTS + filename

        jsonStr = json.dumps(output_list)
        with open(output_file, "w") as f:
            print(jsonStr, file=f)
        print("Output-file successfully created !")


    def write_to_file(self,query,data):
        PATH_TO_RESULTS = "Results/Shodan/"
        self.query = query

        filename = 'list-' + data[0] + '.txt'
        output_file = PATH_TO_RESULTS + filename

        with open(output_file, "w") as f:
            print(query, file=f)
        print("Output-file successfully created !")

    def shodan_search(self, query):

        self.query = query
        output = []
        try:
                # Search Shodan
                results = self.api.search(self.query) #search method returns ShodanSearchResult object that has properties

                # Show the results
                output.append({"Total Results Found" : str(results['total'])})
                for result in results['matches']:
                    output.append({"IPs" : result['ip_str']})
                    output.append({"Hostnames" : result.get('hostnames', '')})
                    output.append({"Organization" : result.get('org', '')})
                    output.append({"Transport Protocol" : result.get('transport', '')})
                    output.append({"Timestamp" : result.get('timestamp', '')})
                    output.append(result.get('location', ''))


        except shodan.APIError as e:
                print('Error: {}'.format(e))

        self.write_to_file_json(self.query,output)


    def shodan_host(self, ip):
        self.ip = ip
        output = []
        try:

                results = self.api.host(self.ip)
                output.append({"IP" : results['ip_str']})
                output.append({"Hostnames" : results.get('hostnames', '')})
                output.append({"OS" : results['os']})
                vulnerabilities = results.get("vulnerabilities", '')
                for result in vulnerabilities:
                    output.append({"CVE" : results['cve']})
                    output.append({"CVSS" : results['cvss']})
                    output.append({"Published" : results['published']})
                    output.append({"Title" : results['title']})


        except shodan.APIError as e:
                print('Error: {}'.format(e))

        self.write_to_file_json(self.ip,output)


    def shodan_domain_info(self,domain):

        self.domain = domain
        output = []
        try:
                domain_info = self.api.dns.domain_info(self.domain)

                # Get the list of IP addresses associated with the domain
                ip_addresses = domain_info['ips']

                # Get the list of subdomains associated with the domain
                subdomains = domain_info['subdomains']

                # Get the list of A records associated with the domain
                a_records = domain_info['a']

                # Get the list of MX records associated with the domain
                mx_records = domain_info['mx']

                # Get the list of NS records associated with the domain
                ns_records = domain_info['ns']

                # Get the date and time the information was last updated
                timestamp = domain_info['timestamp']

                # Do something with the information
                output.append({"IP addresses" : ip_addresses})
                output.append({"Subdomains" : subdomains})
                output.append({"A records" : a_records})
                output.append({"MX records" : mx_records})
                output.append({"NS records" : ns_records})
                output.append({"Timestamp" : timestamp})


        except shodan.APIError as e:
                print('Error: {}'.format(e))

        self.write_to_file_json(self.domain,output)


    def shodan_resolve(self, hostnames):
        RESOLVE_URL = "https://api.shodan.io/dns/resolve"

        self.apiClient = ApiClient(RESOLVE_URL)
        self.hostnames = hostnames

        query = {
            "hostnames": self.hostnames,
            "key": self.api_key
        }

        self.write_to_file(self.apiClient.get(query),self.hostnames)


    def shodan_reverse(self,ips):
        REVERSE_URL = "https://api.shodan.io/dns/reverse"

        self.apiClient = ApiClient(REVERSE_URL)
        self.ips = ips

        #str_ips = str(ips)

        query = {
            "ips": self.ips,
            "key": self.api_key
        }

        self.write_to_file(self.apiClient.get(query),self.ips)
