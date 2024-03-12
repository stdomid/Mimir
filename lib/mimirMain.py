from colorama import Fore
import os
from lib import mimirLib
from lib import mimirSys

banner =Fore.WHITE+"""
███╗░░░███╗██╗███╗░░░███╗██╗██████╗░
████╗░████║██║████╗░████║██║██╔══██╗
██╔████╔██║██║██╔████╔██║██║██████╔╝
██║╚██╔╝██║██║██║╚██╔╝██║██║██╔══██╗
██║░╚═╝░██║██║██║░╚═╝░██║██║██║░░██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝
Mímisbrunnr
OmidRanjbar(Zed)
""" 
infoG = mimirLib.infoG


def clearScreen():
	mimirSys.clearScreen()

menu = Fore.RED+"""
[1] - Whois Domain
[2] - Domain Name
[3] - Robots Content
[4] - Scan Important Url 
[5] - Port Scan
[6] - DNS Lookpu
[Ctrl + z] - Exit
"""



def mimirMain(argument):
	match argument:
		case 1:
			clearScreen()
			print(banner)
			inp = input("Enter url :")
			infoG.getWhoisInfo(inp)
			input("")
		case 2:
			clearScreen()
			print(banner)
			inp = input("Enter IP Address :")
			infoG.getDomainName(inp)
			input("")
		case 3:
			clearScreen()
			print(banner)
			inp = input("Enter url :")
			infoG.robotsContent(inp)
			input("")
		case 4:
			clearScreen()
			print(banner)
			inp = input("Enter url :")
			infoG.robotsScan(inp)
			input("")
		case 5: 
			clearScreen()
			print(banner)
			inp = input("Enter url :")
			infoG.portScan(inp)
			input("")
		case 6:
			clearScreen()
			print(banner)
			inp = input("Enter url :")
			infoG.dnsLookup(inp)
			input("")
		case 7:
			pass

