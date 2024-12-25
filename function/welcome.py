from colorama import init, Fore, Back, Style
import time

# เริ่มต้น colorama
init(autoreset=True)

# ฟังก์ชันแสดงข้อความในสไตล์ต่างๆ
def flashy_message():
    # ทำให้ข้อความกระพริบด้วยสีแดง
    for i in range(5):  # กระพริบ 5 ครั้ง
        time.sleep(0.5)
        print("\033[F", end="")  # ย้อนกลับไปบรรทัดก่อนหน้าเพื่อทับข้อความ

    # พิมพ์ข้อความในพื้นหลังสีเขียวและตัวอักษรสีดำ
    print(Back.GREEN + Fore.BLACK + "📍 เติมเครดิต ติดต่อแอดมิน: https://www.facebook.com/earthkcc147?mibextid=ZbWKwL")
    # พิมพ์ข้อความสว่างในรูปแบบตัวเอียง (emphasized) ใช้ฟอนต์ที่เบลอๆ
    print(Style.BRIGHT + Fore.YELLOW + "🔥 เติมเครดิตวันนี้ รับโบนัสพิเศษ!")

# เรียกใช้ flashy_message()
flashy_message()