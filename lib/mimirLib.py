from requests import get
import socket
import dns.resolver


class infoG: 
    
    def getWhois(url) -> object:
        try:
            outReq = get(f"http://ipwho.is/{url}")
            if outReq.status_code == 200:
                return outReq.text
            else:
                return "Check your internet connction!!"
        except Exception:
            return "Check your internet connction!!"
        
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


    
    
    
