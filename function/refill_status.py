import requests
import os

# ฟังก์ชันสำหรับตรวจสอบสถานะการเติมเงิน
def get_refill_status(api_key):
    # รับ Refill IDs จากผู้ใช้
    refill_ids = input("🔍 กรุณากรอก Refill IDs (คั่นด้วยเครื่องหมายจุลภาค): ").strip()
    
    # ตรวจสอบว่าผู้ใช้กรอกข้อมูลหรือไม่
    if not refill_ids:
        print("❌ กรุณากรอก Refill IDs!")
        return

    api_url = os.getenv("API_URL")
    payload = {
        "key": api_key,
        "action": "refill_status",
        "refills": refill_ids
    }

    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            refill_status_data = response.json()
            print("\n🎉 --- สถานะการเติมเงิน --- 🎉")
            for item in refill_status_data:
                refill = item.get("refill")
                status = item.get("status")
                if isinstance(status, dict) and "error" in status:
                    print(f"❌ Refill ID {refill}: {status['error']}")
                else:
                    print(f"✅ Refill ID {refill}: สถานะ - {status}")
        else:
            print(f"❌ การตรวจสอบสถานะล้มเหลว: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {str(e)}")