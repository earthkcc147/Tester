import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึงค่า Webhook URL จาก .env
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Discord Webhook URL
# DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"  # แทนที่ด้วย Webhook URL ของคุณ

# ฟังก์ชันเพื่อส่งข้อความไปยัง Discord
def send_discord_message(message):
    data = {
        "content": message  # ข้อความที่จะส่ง
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:  # 204 แปลว่าส่งสำเร็จ
            print("ส่งข้อความไปที่ Discord สำเร็จ ✅")
        else:
            print(f"เกิดข้อผิดพลาด: {response.status_code} ❌")
            print(response.text)
    except requests.RequestException as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e} ❌")

# ฟังก์ชันเพื่อรับเวลาปัจจุบันในรูปแบบที่ต้องการ
def get_current_time():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")  # รูปแบบเวลา: YYYY-MM-DD HH:mm:ss
