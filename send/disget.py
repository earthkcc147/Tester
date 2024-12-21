import requests
from datetime import datetime
from dotenv import load_dotenv
import os
from get.get import get_full_info  # นำเข้า get_device_info จาก get.py

# เรียกข้อมูลจาก get_full_info
device_info = get_full_info()

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึงค่า Webhook URL จาก .env
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# ฟังก์ชันเพื่อส่ง Embed ไปยัง Discord
def smdc(embed_data):
    data = {
        "embeds": [embed_data]  # ส่งข้อมูลในรูปแบบ Embed
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

# ฟังก์ชันตกแต่งข้อความ Embed
def print_welcome_message(username):
    current_time = get_current_time()  # รับเวลาปัจจุบัน
    embed_message = {
        "title": f"🎉 ผู้ใช้ {username} เข้าสู่ระบบสำเร็จ ✅",
        "description": f"🕒 เวลา: {current_time}",
        "color": 65280,  # สีเขียวในรูปแบบ Decimal
        "fields": [
            {"name": "📍 IP", "value": device_info['IP'], "inline": False},
            {
                "name": "🌏 ตำแหน่ง",
                "value": f"{device_info['Location']['city']}, {device_info['Location']['region']}, {device_info['Location']['country']}",
                "inline": False,
            },
            {
                "name": "💻 ระบบปฏิบัติการ",
                "value": f"{device_info['Device']['os']} {device_info['Device']['os_version']}",
                "inline": True,
            },
            {
                "name": "🔧 CPU",
                "value": f"{device_info['Device']['processor']} ({device_info['Device']['cpu_count']} cores)",
                "inline": True,
            },
            {
                "name": "🔋 แบตเตอรี่",
                "value": device_info['Battery'],
                "inline": True,
            },
            {
                "name": "🖥️ ความละเอียดหน้าจอ",
                "value": device_info['Screen Resolution'],
                "inline": True,
            },
            {
                "name": "💾 RAM",
                "value": f"{device_info['Device']['memory']} (Used: {device_info['Memory']['used']} GB, Free: {device_info['Memory']['free']} GB, Usage: {device_info['Memory']['percent']}%)",
                "inline": False,
            },
            {
                "name": "🌐 เครือข่าย",
                "value": device_info['Network'],
                "inline": False,
            },
            {
                "name": "💻 GPU",
                "value": device_info['GPU2'],
                "inline": True,
            },
            {
                "name": "💾 การใช้งานดิสก์",
                "value": device_info['Disk Usage2'],
                "inline": True,
            },
        ],
    }

    # ส่ง Embed ไปยัง Discord
    smdc(embed_message)

# ตัวอย่างการเรียกใช้ฟังก์ชัน
# print_welcome_message("example_user")