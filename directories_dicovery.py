import requests


target_url = input('[*] Enter Target URL: ')
wordlist = input('[*] Enter Name Of The Wordlist To Use: ')


def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass


file = open(wordlist, 'r')
for line in file:
	directory = line.strip()
	full_url = target_url + '/' + directory
	response = request(full_url)
	if response:
		print('[*] Discovered Directory At This Path: ' + full_url)
