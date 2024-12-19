import os
import json
import requests
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

# อ่านค่าจาก .env
API_URL = os.getenv("API_URL")
USERS_JSON = os.getenv("USERS")

# แปลงข้อมูล USERS_JSON เป็น dictionary
try:
    users_data = json.loads(USERS_JSON)
except json.JSONDecodeError:
    print("ไม่สามารถแปลงข้อมูล USERS จาก .env ได้ ❌")
    exit()

# รับ username และ password จากผู้ใช้
username = input("กรุณากรอก Username: ")
password = input("กรุณากรอก Password: ")

# ตรวจสอบ username และ password
if username not in users_data or users_data[username]['password'] != password:
    print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง ❌")
    exit()

# ดึงข้อมูลผู้ใช้ปัจจุบัน
current_user = users_data[username]
api_key = current_user['api_key']
products = current_user['products']
user_bm = float(current_user.get('BM', 100))  # ค่า BM เฉพาะของผู้ใช้ (ค่าเริ่มต้น 100)

print(f"ยินดีต้อนรับ {username}! ✅")

# ฟังก์ชันดึงยอดเงินจาก API
def get_balance(api_k):
    data_balance = {
        "key": api_k,
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

    if quantity < min_quantity or quantity > max_quantity:
        print(f"จำนวนสินค้าต้องอยู่ระหว่าง {min_quantity} ถึง {max_quantity} ชิ้น ❌")
        return

    if 'price_per_rate' in product:
        price_per_rate = product['price_per_rate']
        rate = product['rate']
        total_price = round(price_per_rate * user_bm / rate * quantity, 2)
    else:
        price_per_rate = product['price_per_unit']
        total_price = round(price_per_rate * quantity, 2)

    balance = get_balance(api_key)
    if balance is None:
        print("ไม่สามารถดึงยอดเงินได้ ❌")
        return

    adjusted_balance = round(balance * user_bm, 2)

    if total_price > adjusted_balance:
        print(f"ยอดเงินไม่เพียงพอในการซื้อสินค้า {product['description']} ❌")
        return

    print(f"\n--- รายละเอียดการสั่งซื้อ ---")
    print(f"สินค้า: {product['description']}")
    print(f"จำนวนที่เลือก: {quantity} ชิ้น")
    print(f"ราคาต่อหน่วย: {price_per_rate:.2f} บาท (rate: {rate})")
    print(f"ราคาทั้งหมด: {total_price:.2f} บาท")
    print(f"ลิงก์ที่กรอก: {link}")
    print(f"ยอดเงินที่คุณมีหลังจากคูณ: {adjusted_balance:.2f} บาท 💳")

    confirm = input("คุณต้องการยืนยันการสั่งซื้อหรือไม่? (y/n): ").lower()
    if confirm != 'y':
        print("ยกเลิกการสั่งซื้อ ❌")
        return

    data_order = {
        "key": api_key,
        "action": "add",
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

# เมนูหลัก
def show_category_menu():
    balance = get_balance(api_key)
    if balance is not None:
        adjusted_balance = round(balance * user_bm, 2)
        print(f"\n--- เมนูหลัก --- ยอดเงิน: {adjusted_balance:.2f} บาท 💳")
    else:
        print("\n--- เมนูหลัก --- ไม่สามารถดึงยอดเงินได้ ❗")

    print("1. Facebook")
    print("2. TikTok")
    print("3. Instagram")
    print("4. Discord")
    print("0. ออกจากโปรแกรม 🚪")

# ลูปหลัก
while True:
    show_category_menu()
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
    else:
        print("ตัวเลือกไม่ถูกต้อง ❌")