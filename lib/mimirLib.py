from requests import get
from colorama import Fore
import socket
import dns.resolver
import whois

class infoG: 

    def getWhoisInfo(url) -> object:
        try:
            w = whois.whois(url)
            print(w)
        except whois.parser.PywhoisError as e:
            print(f"Error retrieving WHOIS information: {e}")

    def getDomainName(ip_address) -> object:
        try:
            domain_name = socket.gethostbyaddr(ip_address)[0]
            return domain_name
        except socket.herror:
            return "No domain name found for the given IP address."

    def portScan(target_host, target_ports) -> object:
        for port in target_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target_host, port))
                if result == 0:
                    print(f"Port {port}: Open")
                else:
                    print(f"Port {port}: Closed")
                sock.close()
            except socket.error:
                print(f"Could not connect to host: {target_host}")
    
    def dnsLookup(url) -> object:
        if url != "":
            result2 = dns.resolver.resolve(url,"NS")
            for i in result2:
                print("NS Record : ",i.to_text())
        else:
            print("Please Enter Url !!")
            
    def robotsScan(url) -> object:
        with open("payloads/robotsPayloads.txt","r") as file:
            payloads = file.read().replace('\n',"").replace(" ","").replace("'","").split(",")
            for pay in payloads:
                req = get("https://"+url+"/"+pay)
                if req.status_code == 200:
                    print(Fore.GREEN+"[+] http://"+url+"/"+pay)
                else:
                    print(Fore.RED+"[-] http://"+url+"/"+pay)



    
    
    
