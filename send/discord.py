import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึงค่า Bot Token และ Channel ID จาก .env
DISCORD_API_URL = os.getenv("DISCORD_API_URL") 
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# ฟังก์ชันเพื่อส่งข้อความไปยัง Discord
def send_discord_message(message):
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "content": message  # ข้อความที่จะส่ง
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:  # ส่งสำเร็จ
            print("ส่งข้อความไปที่ Discord สำเร็จ ✅")
        else:
            print(f"เกิดข้อผิดพลาด: {response.status_code} ❌")
            print(response.json())
    except requests.RequestException as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e} ❌")

# ฟังก์ชันเพื่อรับเวลาปัจจุบันในรูปแบบที่ต้องการ
def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")  # รูปแบบเวลา: YYYY-MM-DD HH:mm:ss
