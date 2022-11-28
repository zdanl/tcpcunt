import requests
import json
import sys

class internetprotocol(class):

    def __init__(self):
        pass

    def obtain_public_ipv4(self):
        endpoint = 'https://ipinfo.io/json'
        response = requests.get(endpoint, verify=True)

        if response.status_code != 200:
            print("[-] Died obtaining public IPv4 address from API")
            sys.exit(1)

        data = response.json()
        print("[+] Obtained public IPv4 address from API %s" %data['ip'])
        return data['ip']
