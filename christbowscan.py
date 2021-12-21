#!/usr/bin/env python3
print("github.com/christbowel")
import time
import socket
import os
import re
import subprocess
import sys
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
subprocess.call('clear', shell=True)
		ipcheck= input ("entrer votre addresse ip")
                print ("tape 1 pour afficher les ports en tests")
                print ("tape 2 pour afficher les ports ouverts")
                print  ("tape 3 pour tester un seul port spécifique")
		print  ("tape 4 pour tester tous les ports entre les valeurs")
		choicescan = input("entrer votre choix--_>")
	
if choicescan == 1:
			print "wait, it will take a moment..."
			for port in xrange(1, 65536):
 				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((ipcheck, port))
				if result == 0:
  					print(port,"ouvert sur l'host")
				else:
					print(port,"non ouvert")
	
		if choicescan == 2:
			print ( veuillez patientez svp....)
			for port in xrange(1, 65536):
	 			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
				result = sock.connect_ex((ipcheck, port))
				if result == 0:
	  				print (bcolors.OKGREEN + ">>> Port ", port, " est ouvett sur ce host, ipcheck	
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print ("syntaxe invalide")
				time.sleep(3)
				subprocess.Popen("exit", shell=True)
	
		if choicescan == 3:
			port = input("enter a port to check > ")
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((ipcheck, port))
			if result == 0:
	  			print bcolors.OKGREEN + ">>> Port ", port, " is open on network ", ipcheck
			else:
				print bcolors.WARNING + "Port ", port, " is not open"
			choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
	
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print "invalid choice, exiting..."
				time.sleep(3)
				subprocess.Popen("exit", shell=True)
	
		if choicescan == 4:
			rangemin = input("enter the minimum port value > ")
			rangemax = input("enter the maximum port value > ")
			for port in xrange(rangemin, rangemax):
	 			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((ipcheck, port))
				if result == 0:
	  				print bcolors.OKGREEN + ">>> Port ", port, " network ", ipcheck
				else:
					print bcolors.WARNING + "Port ", port, " n'est pas ouvert"			choix = raw_input("Press [Q] to quit, [M] to go to previous menu, and [D] to go to main menu > ")
	
			if choix in ("q", "Q"):
				subprocess.Popen("exit", shell=True)
			elif choix in ("m", "M"):
				choice1()
			elif choix in ("d", "D"):
				mainmenu()
			else:
				print ("syntaxe invalide")
				time.sleep(3)
				subprocess.Popen("exit", shell=True)

print("par christ bowel | github.com/christbowel ")

