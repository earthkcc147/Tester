# ระบบล็อคอินและสั่งซื้อสินค้า

## เกี่ยวกับโปรเจค
โปรเจคนี้เป็นระบบล็อคอินที่มีฟังก์ชันการสั่งซื้อสินค้าออนไลน์ โดยใช้ข้อมูลจาก API ในการดึงข้อมูลสินค้าและตรวจสอบยอดเงินของผู้ใช้ ก่อนทำการสั่งซื้อสินค้า ระบบจะแสดงข้อมูลต่างๆ เช่น รายละเอียดสินค้า, ราคาต่อหน่วย, จำนวนที่ต้องการซื้อ, และเครดิตที่ผู้ใช้มี

## ฟีเจอร์
- ระบบล็อคอินผู้ใช้ด้วย Username และ Password
- ดึงข้อมูลอุปกรณ์ที่ผู้ใช้เข้าสู่ระบบจาก API (เช่น IP, ตำแหน่งที่ตั้ง, ระบบปฏิบัติการ, CPU, RAM)
- การสั่งซื้อสินค้าจาก API โดยตรวจสอบยอดเงินและการยืนยันการสั่งซื้อ
- ระบบการแจ้งเตือนผ่าน Discord และ Line เมื่อมีการสั่งซื้อสำเร็จ

## เทคโนโลยีที่ใช้
- Python 3.x
- Requests (สำหรับการเชื่อมต่อกับ API)
- dotenv (สำหรับการจัดการกับไฟล์ .env)
- colorama (สำหรับการเพิ่มสีในคอนโซล)
- getpass (เพื่อรับรหัสผ่านโดยไม่แสดงผลในคอนโซล)
- datetime (สำหรับการดึงเวลาปัจจุบัน)
- send.discord (สำหรับส่งข้อความไปยัง Discord)
- send.line (สำหรับส่งข้อความไปยัง Line)

## การติดตั้ง
1. คล clone โปรเจคไปที่เครื่องของคุณ:
   ```bash
   git clone https://github.com/your-username/your-repository.git


2. ติดตั้ง dependencies:

pip install -r requirements.txt

สร้างไฟล์ไฟล์ requirements.txt:
requests
python-dotenv
colorama
discord.py
line-bot-sdk

หรือหากต้องการติดตั้งแยกตามโมดูล ให้ใช้คำสั่งดังนี้บนคอนโซล:

pip install requests pip install python-dotenv pip install colorama pip install discord.py pip install line-bot-sdk


3. สร้างไฟล์ .env และกำหนดค่า API_URL, USERS และอื่นๆ ตามที่โปรเจคต้องการ:

API_URL=https://your-api-url.com
USERS={"username": {"password": "your-password", "api_key": "your-api-key", ...}}



การใช้งาน

1. รันโปรเจค:

python main.py


2. เมื่อเข้าสู่ระบบแล้ว ผู้ใช้สามารถเลือกหมวดหมู่สินค้าและทำการสั่งซื้อสินค้าผ่าน API ได้



วิธีการใช้งาน API

ใช้ฟังก์ชัน get_balance เพื่อตรวจสอบยอดเงินที่ผู้ใช้มี

ใช้ฟังก์ชัน place_order เพื่อลงรายการสั่งซื้อสินค้า


การสนับสนุน

หากคุณมีคำถามหรือปัญหาเกี่ยวกับโปรเจคนี้ สามารถติดต่อผู้พัฒนาได้ที่:

Facebook: Earth KCC

Email: your-email@example.com


ใบอนุญาต

โปรเจคนี้เป็นโปรเจคโอเพนซอร์สภายใต้ MIT License.

### หมายเหตุ:
- แทนที่ URL และข้อมูลในส่วนต่างๆ (เช่น `your-username`, `your-email@example.com`, และ `API_URL`) ให้เหมาะสมกับโปรเจคของคุณ
- หากโปรเจคมีไฟล์ `LICENSE` ให้แน่ใจว่ามีไฟล์นั้นอยู่ใน repository เพื่อให้ลิงก์ `MIT License` ทำงานได้
