import os
import json
import requests

# ฟังก์ชันตรวจสอบสถานะคำสั่งซื้อ
def check_multiple_order_status():
    # อ่านค่า API_URL จาก environment variable
    api_url = os.getenv("API_URL")
    if not api_url:
        print("❌ ไม่พบ API_URL ใน environment variable.")
        return

    while True:
        # รับค่า Order IDs จากผู้ใช้
        order_ids = input("🔍 กรุณากรอก Order IDs (คั่นด้วยเครื่องหมาย ,) หรือพิมพ์ 00 เพื่อกลับ: ")
        if order_ids.strip() == "00":
            print("🔙 กลับสู่เมนูหลัก.")
            return
        elif not order_ids.strip():
            print("❌ กรุณากรอก Order IDs อย่างน้อยหนึ่งรายการ.")
            continue

        # กำหนดพารามิเตอร์สำหรับคำขอ
        payload = {
            "key": api_url,
            "action": "status",
            "orders": order_ids
        }

        try:
            # ส่งคำขอ POST ไปยัง API
            response = requests.post(api_url, data=payload)
            response_data = response.json()

            # ตรวจสอบผลลัพธ์และแสดงข้อมูล
            print("\n🎉 --- สถานะคำสั่งซื้อ --- 🎉")
            for order_id, details in response_data.items():
                if "error" in details:
                    print(f"❌ Order ID: {order_id} - {details['error']}")
                else:
                    print(
                        f"✅ Order ID: {order_id}\n"
                        f"   - Charge: {details['charge']} {details['currency']}\n"
                        f"   - Start Count: {details['start_count']}\n"
                        f"   - Status: {details['status']}\n"
                        f"   - Remains: {details['remains']}"
                    )
        except requests.exceptions.RequestException as e:
            print(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อกับ API: {e}")
        except json.JSONDecodeError:
            print("❌ ไม่สามารถแปลงผลลัพธ์จาก API เป็น JSON ได้.")

# เรียกฟังก์ชันเพื่อทดสอบ
# check_multiple_order_status()