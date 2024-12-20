import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# โหลดค่าจากไฟล์ .env
load_dotenv()

# Line Messaging API
LINE_API_URL = os.getenv("LINE_API_URL") 
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")  # ใส่ Channel Access Token ในไฟล์ .env
LINE_GROUP_ID = os.getenv("LINE_GROUP_ID")  # ใส่ Group ID ในไฟล์ .env

# ฟังก์ชันเพื่อส่งข้อความไปยัง line
def send_line_message(message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    data = {
        "to": LINE_GROUP_ID,
        "messages": [{
            "type": "text",
            "text": message
        }]
    }
    try:
        response = requests.post(LINE_API_URL, headers=headers, json=data)
        if response.status_code == 200:
            print("ส่งข้อความไปที่ Line สำเร็จ ✅")
        else:
            print(f"เกิดข้อผิดพลาด: {response.status_code} ❌")
            print(response.json())
    except requests.RequestException as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e} ❌")

# ฟังก์ชันเพื่อรับเวลาปัจจุบันในรูปแบบที่ต้องการ
def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")  # รูปแบบเวลา: YYYY-MM-DD HH:mm:ss