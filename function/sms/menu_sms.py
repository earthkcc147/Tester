import requests
import os

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')


# เมนู SMS
def show_sms_menu():
    while True:
        clear_console()
        print("\n📱 --- เมนู SMS --- 📱\n")
        print("1. sms 42 api")
        print("00. ย้อนกลับ")

        try:
            sms_choice = int(input("\n🔔 กรุณาเลือกตัวเลือก: "))

            if sms_choice == 00:
                print("🔙 กลับสู่เมนูหลัก...")
                break
            elif sms_choice == 1: 
                print("กำลังรันไฟล์ sms.py...")
                subprocess.run(["python3", "function/sms/sms.py"])
            else:
                print("❌ ตัวเลือกไม่ถูกต้อง กรุณาลองอีกครั้ง!")
        except ValueError:
            print("❌ กรุณากรอกตัวเลขเท่านั้น!")

# show_sms_menu()