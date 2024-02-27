from lib import mimirMain
from lib import mimirSys
from colorama import Fore

banner = mimirMain.banner
menu = mimirMain.menu

def clearScreen():
    mimirSys.clearScreen()

while 1:
	if 1 == 1 :
		clearScreen()
		print(banner)
		print(menu)
		inp =  input(Fore.WHITE+"\nEnter _> ")
		mimirMain.mimirMain(int(inp))
		print(inp)

