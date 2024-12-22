import os
import requests

# ฟังก์ชันดึงสถานะคำสั่งซื้อจาก API
def get_order_status(order_id):
    # ใช้ค่า API URL จาก .env หรือตั้งค่าล่วงหน้า
    api_url = os.getenv("API_URL")  # ตั้งค่า API_URL
    api_key = os.getenv("API_KEY")  # ตั้งค่า API_KEY
    
    # ข้อมูลที่ใช้ในการร้องขอ
    params = {
        "key": api_key,
        "action": "status",
        "order": order_id
    }

    # ส่งคำขอไปยัง API
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # เช็คว่าไม่มีข้อผิดพลาดในการตอบกลับ
        return response.json()  # คืนค่าผลลัพธ์ในรูปแบบ JSON
    except requests.exceptions.RequestException as e:
        print(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อกับ API: {e}")
        return None

# ฟังก์ชันแสดงผลสถานะคำสั่งซื้อ
def show_order_status():
    order_id = input("🔍 กรุณากรอก Order ID เพื่อตรวจสอบสถานะคำสั่งซื้อ: ")
    
    # เรียกฟังก์ชันเพื่อดึงข้อมูลสถานะคำสั่งซื้อ
    order_status = get_order_status(order_id)
    
    if order_status:
        print("\n🎉 --- สถานะคำสั่งซื้อ --- 🎉")
        print(f"💳 Charge: {order_status.get('charge')}")
        print(f"⏳ Start Count: {order_status.get('start_count')}")
        print(f"📦 Status: {order_status.get('status')}")
        print(f"💰 Remaining: {order_status.get('remains')} {order_status.get('currency')}")
    else:
        print("❌ ไม่สามารถดึงข้อมูลสถานะคำสั่งซื้อได้!")