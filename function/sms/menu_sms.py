# เมนู SMS
def show_sms_menu():
    while True:
        clear_console()
        print("\n📱 --- เมนู SMS --- 📱\n")
        print("1. สวัสดี")
        print("2. ย้อนกลับ")

        try:
            sms_choice = int(input("\n🔔 กรุณาเลือกตัวเลือก: "))

            if sms_choice == 1:
                print("👋 สวัสดี! ยินดีต้อนรับสู่เมนู SMS")
            elif sms_choice == 2:
                print("🔙 กลับสู่เมนูหลัก...")
                break
            else:
                print("❌ ตัวเลือกไม่ถูกต้อง กรุณาลองอีกครั้ง!")
        except ValueError:
            print("❌ กรุณากรอกตัวเลขเท่านั้น!")

# show_sms_menu()