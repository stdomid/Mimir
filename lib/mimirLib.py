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
            print(domain_name)
        except socket.herror:
            print("No domain name found for the given IP address.")

    def portScan(target_host) -> object:
        for port in [21,22,23,25,53,80,443,3070,5060,135,139,1433,1521,1723,1900,2302,3389,3306,4000,4444,5000,5555,5900,6667,6697,8000,8081,9100,9090,5900,445,5985,598]:
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

    def robotsContent(url) -> object:
        if url != "":
            req = get("https://"+url+"/robots.txt")
            if req.status_code == 200:
                print("\nresults for this url http://"+url+"/robots.txt :\n")
                print(req.text)
            else:
                print("\nSomething's wrong !\n")
                print("Check your url")  
                print("Check your internet connection")  
        else:
            print("This url does not have robots.txt file")     





    
    
    
