import os
import json
import requests
import webbrowser
from dotenv import load_dotenv
from colorama import init, Fore, Style
from getpass import getpass  # เพิ่มการใช้งาน getpass

# เริ่มต้น colorama
init(autoreset=True)

# โหลดค่าจากไฟล์ .env
load_dotenv()

# อ่านค่าจาก .env
API_URL = os.getenv("API_URL")
USERS_JSON = os.getenv("USERS")

# แปลงข้อมูล USERS_JSON เป็น dictionary
try:
    users_data = json.loads(USERS_JSON)
except json.JSONDecodeError:
    print(Fore.RED + "ไม่สามารถแปลงข้อมูล USERS จาก .env ได้ ❌")
    exit()

# ฟังก์ชันตกแต่งข้อความ
def print_welcome_message(username):
    print(Fore.GREEN + Style.BRIGHT + f"\nยินดีต้อนรับ {username}!\n")
    print(Fore.YELLOW + "เข้าสู่ระบบสำเร็จ ✅\n")

# สร้างหน้าจอล็อคอินที่สวยงาม
def login_screen():
    print(Fore.CYAN + "="*40)
    print(Fore.MAGENTA + Style.BRIGHT + "         ระบบล็อคอิน")
    print(Fore.CYAN + "="*40)
    print(Fore.WHITE + "ติดต่อแอดมินเพื่อสมัครสมาชิก\n   https://www.facebook.com/earthkcc147?mibextid=ZbWKwL"\n)
    print(Fore.WHITE + "กรุณากรอกข้อมูลเพื่อเข้าสู่ระบบ")


# แสดงหน้าล็อคอิน
login_screen()

# รับ username และ password จากผู้ใช้
username = input(Fore.YELLOW + "กรุณากรอก Username: ")
# รับ password โดยใช้ getpass เพื่อซ่อนรหัสผ่าน
password = getpass(Fore.YELLOW + "กรุณากรอก Password: ")

# password = input(Fore.YELLOW + "กรุณากรอก Password: ")

# ตรวจสอบ username และ password
if username not in users_data or users_data[username]['password'] != password:
    print(Fore.RED + "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง ❌")
    exit()

# ดึงข้อมูลผู้ใช้ปัจจุบัน
current_user = users_data[username]
api_key = current_user['api_key']
products = current_user['products']
BM = float(current_user.get('BM', 100))  # ดึงค่าตัวคูณ BM จากข้อมูลผู้ใช้

# แสดงข้อความต้อนรับ
print_welcome_message(username)


# ฟังก์ชันดึงยอดเงินจาก API
def get_balance(api_k):
    data_balance = {
        "key": api_key,
        "action": "balance"
    }

    try:
        response_balance = requests.post(API_URL, data=data_balance)
        if response_balance.status_code == 200:
            balance_data = response_balance.json()
            if 'balance' in balance_data:
                return round(float(balance_data['balance']), 2)
    except requests.RequestException as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e} ❌")
    return None

# ฟังก์ชันการสั่งซื้อสินค้า
def place_order(category, product_key, quantity, link):
    product = products[category][product_key]
    min_quantity = product['min_quantity']
    max_quantity = product['max_quantity']

    # ตรวจสอบว่าจำนวนสินค้าที่เลือกอยู่ในช่วงที่อนุญาต
    if quantity < min_quantity or quantity > max_quantity:
        print(f"จำนวนสินค้าต้องอยู่ระหว่าง {min_quantity} ถึง {max_quantity} ชิ้น ❌")
        return

    # คำนวณราคาตาม price_per_rate และ rate
    if 'price_per_rate' in product:
        price_per_rate = product['price_per_rate']
        rate = product['rate']
        total_price = round(price_per_rate * BM / rate * quantity, 2)
    else:
        price_per_rate = product['price_per_unit']
        total_price = round(price_per_rate * quantity, 2)

    balance = get_balance(api_key)
    if balance is None:
        print("ไม่สามารถดึงยอดเงินได้ ❌")
        return

    # คูณยอดเงินด้วยตัวคูณ
    adjusted_balance = round(balance * BM, 2)

    if total_price > adjusted_balance:
        print(f"ยอดเงินไม่เพียงพอในการซื้อสินค้า {product['description']} ❌")
        return

    # แสดงรายละเอียดการสั่งซื้อให้ผู้ใช้ยืนยัน
    print(f"\n--- รายละเอียดการสั่งซื้อ ---")
    print(f"สินค้า: {product['description']}")
    print(f"จำนวนที่เลือก: {quantity} ชิ้น")
    print(f"ราคาต่อหน่วย: {price_per_rate:.2f} บาท (rate: {rate})")
    print(f"ราคาทั้งหมด: {total_price:.2f} บาท")
    print(f"ลิงก์ที่กรอก: {link}")
    print(f"ยอดเงินที่คุณมีหลังจากคูณ: {adjusted_balance:.2f} บาท 💳")

    # การยืนยันการสั่งซื้อ
    confirm = input("คุณต้องการยืนยันการสั่งซื้อหรือไม่? (y/n): ").lower()
    if confirm != 'y':
        print("ยกเลิกการสั่งซื้อ ❌")
        return

    # ข้อมูลการสั่งซื้อที่ต้องการส่งไปยัง API
    data_order = {
        "key": api_key,
        "action": product['action'],
        "service": product['service'],
        "link": link,
        "quantity": quantity
    }

    try:
        response_order = requests.post(API_URL, data=data_order)
        if response_order.status_code == 200:
            order_data = response_order.json()
            if 'order' in order_data:
                remaining_balance = round(adjusted_balance - total_price, 2)
                print(f"การสั่งซื้อสำเร็จ! คำสั่งซื้อ ID: {order_data['order']} ✅")
                print(f"รวมราคาทั้งหมด: {total_price:.2f} บาท 💵")
                print(f"ยอดเงินที่เหลือหลังจากการสั่งซื้อ: {remaining_balance:.2f} บาท 💳")
            else:
                print("การสั่งซื้อไม่สำเร็จ ❌")
        else:
            print("เกิดข้อผิดพลาดในการสั่งซื้อ ❌")
    except requests.RequestException as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e} ❌")

# ฟังก์ชันเลือกสินค้า
def choose_product(category):
    if category not in products:
        print("ไม่มีสินค้าในหมวดหมู่นี้ ❌")
        return

    category_products = products[category]
    print("\n--- รายการสินค้า ---")
    for index, (product_name, details) in enumerate(category_products.items(), start=1):
        print(f"{index}. {details['description']} - ราคา: {details['price_per_rate']:.2f} บาท ต่อ {details['min_quantity']}")
        print(f"   จำนวนขั้นต่ำ: {details['min_quantity']} - จำนวนสูงสุด: {details['max_quantity']}")
        if 'example_link' in details:
            print(f"   ตัวอย่างลิงก์: {details['example_link']}")

    print("0. ย้อนกลับ 🔙")

    choice = int(input("กรุณาเลือกสินค้าที่ต้องการ: "))
    if choice == 0:
        return

    if 1 <= choice <= len(category_products):
        product_key = list(category_products.keys())[choice - 1]
        product = category_products[product_key]
        print(f"คุณเลือก {product['description']}")

        min_quantity = product['min_quantity']
        max_quantity = product['max_quantity']
        price_per_rate = product['price_per_rate']
        print(f"จำนวนขั้นต่ำ: {min_quantity}, จำนวนสูงสุด: {max_quantity}")
        print(f"ราคาต่อหน่วย: {price_per_rate:.2f} บาท")

        link = input(f"กรุณากรอกลิงก์ที่ต้องการ (ตัวอย่าง: {product['example_link'] if 'example_link' in product else 'ไม่มีตัวอย่าง'}): ")
        quantity = int(input(f"กรุณากรอกจำนวนที่ต้องการซื้อ (ระหว่าง {min_quantity} และ {max_quantity}): "))
        place_order(category, product_key, quantity, link)

# เมนูหลัก
def show_category_menu():
    balance = get_balance(api_key)
    if balance is not None:
        adjusted_balance = round(balance * BM, 2)
        print(f"\n--- เมนูหลัก --- ยอดเงิน: {adjusted_balance:.2f} บาท 💳")
    else:
        print("\n--- เมนูหลัก --- ไม่สามารถดึงยอดเงินได้ ❗")

    print("1. Facebook")
    print("2. TikTok")
    print("3. Instagram")
    print("4. Discord")
    print("99. เพื่อติดต่อแอดมิน")
    print("0. ออกจากโปรแกรม 🚪")

# ลูปหลัก
while True:
    show_category_menu()
    try:
        category_choice = int(input("กรุณาเลือกหมวดหมู่สินค้า: "))

        if category_choice == 0:
            print("ออกจากโปรแกรม 👋")
            break
        elif category_choice == 1:
            choose_product("facebook")
        elif category_choice == 2:
            choose_product("tiktok")
        elif category_choice == 3:
            choose_product("instagram")
        elif category_choice == 4:
            choose_product("discord")
        elif category_choice == 99:
            print("https://www.facebook.com/earthkcc147?mibextid=ZbWKwL")
        else:
            print("ตัวเลือกไม่ถูกต้อง ❌")
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น ❌")