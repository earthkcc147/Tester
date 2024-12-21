import json
import requests
import base64
from dotenv import load_dotenv
import os

# โหลดตัวแปรจากไฟล์ .env
load_dotenv()

repo_owner = os.getenv("REPO_OWNER")
repo_name = os.getenv("REPO_NAME")
file_path = os.getenv("FILE_PATH")
token = os.getenv("GITHUB_TOKEN")

def save_order_to_file(order_data, repo_owner, repo_name, file_path, token):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
    response = requests.get(url, headers={'Authorization': f'token {token}'})

    if response.status_code == 200:
        file_info = response.json()
        file_content = file_info['content']
        file_sha = file_info['sha']
        file_data = base64.b64decode(file_content).decode('utf-8')
        orders = json.loads(file_data)
    else:
        orders = []
        file_sha = None

    orders.append(order_data)

    new_content = json.dumps(orders, ensure_ascii=False, indent=4)
    encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')

    update_data = {
        'message': 'Update save.json with new order data',
        'content': encoded_content,
        'sha': file_sha
    }

    update_response = requests.put(url, json=update_data, headers={'Authorization': f'token {token}'})

    if update_response.status_code == 200:
        print("ไฟล์ save.json ถูกอัปเดตเรียบร้อยแล้ว!")
    else:
        print(f"เกิดข้อผิดพลาด: {update_response.json()}")


# save_order_to_file(order_data, repo_owner, repo_name, file_path, token)