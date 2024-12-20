import psutil
import requests
import platform
import ctypes
import psutil

# ฟังก์ชันดึงข้อมูล RAM
def get_memory_info():
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)  # แปลงหน่วยเป็น GB
    available_memory = memory.available / (1024 ** 3)  # แปลงหน่วยเป็น GB
    used_memory = memory.used / (1024 ** 3)  # แปลงหน่วยเป็น GB
    return f"หน่วยความจำทั้งหมด: {total_memory:.2f} GB, ใช้ไป: {used_memory:.2f} GB, ว่าง: {available_memory:.2f} GB"

# ฟังก์ชันดึงข้อมูลแบตเตอรี่
def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        battery_percent = battery.percent
        plugged = battery.power_plugged
        remaining_time = battery.secsleft / 60 if battery.secsleft != psutil.POWER_TIME_UNLIMITED else None
        
        status = "ชาร์จเต็ม" if plugged else "ชาร์จไม่เต็ม"
        
        # ถ้ามีเวลาในการชาร์จที่เหลือ
        time_left = f"{remaining_time:.0f} นาที" if remaining_time else "ไม่สามารถคำนวณเวลาได้"
        
        return f"แบตเตอรี่: {battery_percent}% ({status}), เวลาในการชาร์จที่เหลือ: {time_left}"
    
    return "ข้อมูลแบตเตอรี่ไม่พร้อมใช้งาน"

# ฟังก์ชันดึงข้อมูล CPU
def get_cpu_info():
    cpu_count = psutil.cpu_count(logical=False)  # จำนวนคอร์ของ CPU
    cpu_freq = psutil.cpu_freq().current  # ความถี่ของ CPU (MHz)
    return f"CPU: {cpu_count} คอร์, ความถี่ {cpu_freq} MHz"

# ฟังก์ชันดึงข้อมูล GPU
def get_gpu_info():
    # สำหรับการใช้งานกับเครื่องที่มี GPU โดยเฉพาะ
    try:
        gpu_info = subprocess.check_output("nvidia-smi --query-gpu=name --format=csv,noheader", shell=True)
        return f"GPU: {gpu_info.decode().strip()}"
    except:
        return "ข้อมูล GPU ไม่สามารถดึงได้"

# ฟังก์ชันดึงข้อมูลจาก IP
def get_ip_info():
    try:
        ip_info = requests.get("https://ipinfo.io/json").json()
        ip = ip_info.get("ip", "ไม่ทราบ IP")
        city = ip_info.get("city", "ไม่ทราบเมือง")
        region = ip_info.get("region", "ไม่ทราบภูมิภาค")
        country = ip_info.get("country", "ไม่ทราบประเทศ")
        return ip, city, region, country
    except:
        return "ไม่สามารถดึงข้อมูล", "ไม่สามารถดึงข้อมูล", "ไม่สามารถดึงข้อมูล", "ไม่สามารถดึงข้อมูล"

# ฟังก์ชันดึงข้อมูลจากอุปกรณ์ทั้งหมด
def get_device_info():
    try:
        ip, city, region, country = get_ip_info()
        user_agent = requests.get("https://httpbin.org/user-agent").json().get("user-agent", "ไม่ทราบอุปกรณ์")
        device_model = platform.system()  # สามารถปรับปรุงหากต้องการข้อมูลอุปกรณ์ที่เจาะจงมากขึ้น
        os, browser = parse_device_details(user_agent)
        screen_resolution = get_screen_resolution()
        connection_speed = get_connection_speed()

        memory_info = get_memory_info()
        battery_info = get_battery_info()
        cpu_info = get_cpu_info()
        gpu_info = get_gpu_info()

        return {
            "ip": ip,
            "location": f"{city}, {region}, {country}",
            "device": user_agent,
            "device_model": device_model,
            "os": os,
            "browser": browser,
            "screen_resolution": screen_resolution,
            "connection_speed": connection_speed,
            "memory_info": memory_info,
            "battery_info": battery_info,
            "cpu_info": cpu_info,
            "gpu_info": gpu_info
        }
    except Exception as e:
        return {
            "ip": "ไม่สามารถดึงข้อมูล",
            "location": "ไม่สามารถดึงข้อมูล",
            "device": "ไม่สามารถดึงข้อมูล",
            "device_model": "ไม่สามารถดึงข้อมูล",
            "os": "ไม่สามารถดึงข้อมูล",
            "browser": "ไม่สามารถดึงข้อมูล",
            "screen_resolution": "ไม่สามารถดึงข้อมูล",
            "connection_speed": "ไม่สามารถดึงข้อมูล",
            "memory_info": "ไม่สามารถดึงข้อมูล",
            "battery_info": "ไม่สามารถดึงข้อมูล",
            "cpu_info": "ไม่สามารถดึงข้อมูล",
            "gpu_info": "ไม่สามารถดึงข้อมูล"
        }








def print_welcome_message(username, device_info):
    current_time = get_current_time()
    print(Fore.GREEN + Style.BRIGHT + f"\nยินดีต้อนรับ {username}!\n")
    print(Fore.YELLOW + "เข้าสู่ระบบสำเร็จ ✅\n")
    print(Fore.CYAN + f"📡 IP: {device_info['ip']}")
    print(Fore.CYAN + f"🌍 ตำแหน่ง: {device_info['location']}")
    print(Fore.CYAN + f"💻 อุปกรณ์: {device_info['device']}")
    print(Fore.CYAN + f"📱 รุ่นอุปกรณ์: {device_info['device_model']}")
    print(Fore.CYAN + f"🔧 ระบบปฏิบัติการ: {device_info['os']}")
    print(Fore.CYAN + f"🌐 เบราว์เซอร์: {device_info['browser']}")
    print(Fore.CYAN + f"🖥️ ความละเอียดหน้าจอ: {device_info['screen_resolution']}")
    print(Fore.CYAN + f"⚡ ความเร็วในการเชื่อมต่อ: {device_info['connection_speed']}")