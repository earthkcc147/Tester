from colorama import init, Fore, Back, Style
import time

# เริ่มต้น colorama
init(autoreset=True)

# ฟังก์ชันแสดงข้อความในสไตล์ต่างๆ
def flashy_message():
    # สีฟ้าและสว่างพร้อมการกระพริบ
    print(Fore.CYAN + Style.BRIGHT + "📍 เติมเครดิต ติดต่อแอดมิน: https://www.facebook.com/earthkcc147?mibextid=ZbWKwL")
    
    # ทำให้ข้อความกระพริบด้วยสีแดง
    for i in range(5):  # กระพริบ 5 ครั้ง
        print(Fore.RED + Style.BRIGHT + "⚠️ โปรดระวัง! คุณต้องเติมเครดิต.")
        time.sleep(0.5)
        print("\033[F", end="")  # ย้อนกลับไปบรรทัดก่อนหน้าเพื่อทับข้อความ

    # พิมพ์ข้อความในพื้นหลังสีเขียวและตัวอักษรสีดำ
    print(Back.GREEN + Fore.BLACK + "✅ การเติมเครดิตสำเร็จ! ขอบคุณที่ใช้บริการ.")
    
    # พิมพ์ข้อความสว่างในรูปแบบตัวเอียง (emphasized) ใช้ฟอนต์ที่เบลอๆ
    print(Style.BRIGHT + Fore.YELLOW + "🔥 เติมเครดิตวันนี้ รับโบนัสพิเศษ!")

# flashy_message()