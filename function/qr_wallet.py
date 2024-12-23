import requests
import os

def download_file_from_google_drive(url, save_path):
    try:
        # ตรวจสอบว่าไฟล์มีอยู่แล้วหรือไม่
        if os.path.exists(save_path):
            print(f"ℹ️ ไฟล์ '{save_path}' มีอยู่แล้ว! ไม่จำเป็นต้องดาวน์โหลดอีกครั้ง")
            return
        
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"✅ ไฟล์ถูกบันทึกที่: {save_path}")
        else:
            print(f"❌ ไม่สามารถดาวน์โหลดไฟล์ได้: {response.status_code}")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {str(e)}")

# ใช้ฟังก์ชัน
download_url = "https://drive.google.com/uc?id=17vHFgWgYdq7ba8U6I_YKrCUyVXrehoAl&export=download"
save_path = "qr_image.jpg"  # เส้นทางที่ต้องการบันทึก
# download_file_from_google_drive(download_url, save_path)