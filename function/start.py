# pip install pyfiglet colorama

import os
import time
import pyfiglet
from colorama import init, Fore

# เริ่มต้นการใช้งาน colorama
init()

# สร้างข้อความ ASCII art ด้วย pyfiglet
intro = pyfiglet.figlet_format("Welcome\nTo\nGumarun Store", font="slant")

# ฟังก์ชันแสดงข้อความพร้อมดีเลย์
def print_intro():
    for line in intro.splitlines():
        print(Fore.YELLOW + line)  # ทำให้ข้อความเป็นสีเหลือง
        time.sleep(0.1)  # เพิ่มดีเลย์เพื่อจำลองแอนิเมชัน


def print_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = '''
   )   (          (        (    )   
  ())  )\  ( (  : )\  (    )\  ((.  
 (()))((_) )\)\  (_() )\  ((_) ))\  
(/ __|(_))(_((_)((_)()( )((_))((_)) 
| (_ | || | '  \/ _` | '_| || | ' \)
 \___|\_._|_|_|_|__/_|_|  \_._|_||_|
                                           
    > Gumarun Store ©
    '''
    print(banner)

# เรียกใช้ฟังก์ชัน
# print_intro()
# input("\nกด Enter เพื่อดำเนินการต่อ...")  # รอผู้ใช้กด Enter
# print_logo()