import json
import os

# ฟังก์ชันดึงข้อมูลจากไฟล์ save.json ตามชื่อผู้ใช้
def show_order_history(username):
    # ตรวจสอบว่าไฟล์ save.json มีอยู่หรือไม่
    if os.path.exists('save.json'):
        with open('save.json', 'r', encoding='utf-8') as f:
            orders = json.load(f)
        
        # กรองคำสั่งซื้อที่ตรงกับชื่อผู้ใช้
        user_orders = [order for order in orders if order.get("name") == username]
        
        # หากพบคำสั่งซื้อของผู้ใช้
        if user_orders:
            print("\n🎉 --- ประวัติการสั่งซื้อของคุณ --- 🎉")
            print("-" * 60)  # เส้นแบ่ง
            for order in user_orders:
                print(f"🛒  Order ID: {order['order_id']}")
                print(f"   หมวดหมู่: {order['category']}")
                print(f"   สินค้า: {order['product']}")
                print(f"   จำนวน: {order['quantity']} ชิ้น")
                print(f"   ราคาทั้งหมด: {order['total_price']} บาท")
                print(f"   เวลาที่สั่งซื้อ: {order['timestamp']}")
                print("-" * 60)  # เส้นแบ่งระหว่างคำสั่งซื้อ
        else:
            print(f"❌ ไม่พบประวัติการสั่งซื้อสำหรับชื่อผู้ใช้นี้: {username}")
    else:
        print("❌ ไม่พบไฟล์ save.json.")

