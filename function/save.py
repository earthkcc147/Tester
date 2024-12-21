import json
import os

def save_order_to_file(order_data):
    # ตรวจสอบว่าไฟล์ save.json มีอยู่หรือไม่
    if not os.path.exists('save.json'):
        # ถ้าไฟล์ยังไม่มี ให้สร้างไฟล์ใหม่และเขียนข้อมูลเริ่มต้น
        with open('save.json', 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

    # อ่านข้อมูลในไฟล์ save.json
    with open('save.json', 'r', encoding='utf-8') as f:
        orders = json.load(f)

    # เพิ่มข้อมูลคำสั่งซื้อใหม่
    orders.append(order_data)

    # บันทึกข้อมูลกลับไปยังไฟล์
    with open('save.json', 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=4)
