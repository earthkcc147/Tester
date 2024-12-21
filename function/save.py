import json
import requests
import base64

repo_owner = "earthkcc147"  # แทนที่ด้วยชื่อผู้ใช้ GitHub ของคุณ
repo_name = "GMR-STORE"  # แทนที่ด้วยชื่อ repository ของคุณ
file_path = "save.json"  # เส้นทางของไฟล์ใน repository
token = "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"  # แทนที่ด้วย GitHub token ที่สร้าง

def save_message_to_file(message, repo_owner, repo_name, file_path, token):
    # ตรวจสอบว่าไฟล์ save.json มีอยู่ใน GitHub หรือไม่
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'

    # ดึงข้อมูลไฟล์จาก GitHub
    response = requests.get(url, headers={'Authorization': f'token {token}'})

    if response.status_code == 200:
        # ถ้าไฟล์มีอยู่แล้ว ให้โหลดข้อมูลไฟล์จาก GitHub
        file_info = response.json()
        file_content = file_info['content']
        file_sha = file_info['sha']

        # ใช้ base64 decoder เพื่อ decode ข้อมูลจาก GitHub
        file_data = base64.b64decode(file_content).decode('utf-8')

        messages = json.loads(file_data)
    else:
        # ถ้าไฟล์ไม่มี ให้สร้างไฟล์ใหม่
        messages = []

    # เพิ่มข้อความใหม่
    messages.append(message)

    # อัปโหลดข้อมูลใหม่ไปยัง GitHub
    new_content = json.dumps(messages, ensure_ascii=False, indent=4)
    encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')

    # ส่งคำขอ PUT ไปยัง GitHub API เพื่ออัปเดตไฟล์
    update_data = {
        'message': 'Update save.json with new message data',
        'content': encoded_content,
        'sha': file_info['sha'] if response.status_code == 200 else None
    }

    update_response = requests.put(url, json=update_data, headers={'Authorization': f'token {token}'})

    if update_response.status_code == 200:
        print("ไฟล์ save.json ถูกอัปเดตเรียบร้อยแล้ว!")
    else:
        print(f"เกิดข้อผิดพลาด: {update_response.json()}")

# ข้อความที่จะบันทึก
# message = {
    "username": "user123",
    "text": "นี่คือข้อความที่ต้องการบันทึก",
    "timestamp": "21-12-2024 18:38:05"
}

# เรียกใช้งานฟังก์ชัน
# save_message_to_file(message, repo_owner, repo_name, file_path, token)