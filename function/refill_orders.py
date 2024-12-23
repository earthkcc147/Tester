import requests
import os

# ฟังก์ชันสำหรับ refill
def refill_orders(api_key):
    # รับ Order IDs จากผู้ใช้
    order_ids = input("🔍 กรุณากรอก Order IDs (คั่นด้วยเครื่องหมายจุลภาค): ").strip()
    
    # ตรวจสอบว่าผู้ใช้กรอกข้อมูลหรือไม่
    if not order_ids:
        print("❌ กรุณากรอก Order IDs!")
        return

    api_url = os.getenv("API_URL")
    payload = {
        "key": api_key,
        "action": "refill",
        "orders": order_ids
    }

    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            refill_data = response.json()
            print("\n🎉 --- ผลการเติมเงิน --- 🎉")
            for item in refill_data:
                order = item.get("order")
                refill = item.get("refill")
                if isinstance(refill, dict) and "error" in refill:
                    print(f"❌ Order ID {order}: {refill['error']}")
                else:
                    print(f"✅ Order ID {order}: เติมเงินสำเร็จ (Refill ID: {refill})")
        else:
            print(f"❌ การเติมเงินล้มเหลว: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {str(e)}")