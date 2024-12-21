import os
import platform
import socket
import requests
from datetime import datetime
import psutil  # ใช้สำหรับข้อมูลระบบ
import shutil  # ใช้ตรวจสอบความละเอียดหน้าจอ

# ฟังก์ชันดึง IP Address
def get_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except requests.RequestException:
        return "ไม่สามารถดึงข้อมูล IP ได้"

# ฟังก์ชันดึงตำแหน่งที่ตั้งจาก IP
def get_location(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/").json()
        return {
            "city": response.get("city", "ไม่ทราบ"),
            "region": response.get("region", "ไม่ทราบ"),
            "country": response.get("country_name", "ไม่ทราบ"),
        }
    except requests.RequestException:
        return {"city": "ไม่ทราบ", "region": "ไม่ทราบ", "country": "ไม่ทราบ"}

# ฟังก์ชันดึงข้อมูลอุปกรณ์
def get_device_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "platform": platform.platform(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(logical=True),
        "memory": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
    }

# ฟังก์ชันดึงข้อมูล GPU (รองรับ Termux/Pydroid3 ที่ไม่มี GPU)
def get_gpu_info():
    try:
        import GPUtil  # ติดตั้งด้วย `pip install gputil`
        gpus = GPUtil.getGPUs()
        return [{"name": gpu.name, "load": f"{gpu.load * 100:.2f}%"} for gpu in gpus]
    except ImportError:
        return "ไม่สามารถดึงข้อมูล GPU ได้ (อาจไม่มี GPU)"

# ฟังก์ชันดึงข้อมูลเบราว์เซอร์
def get_browser_info():
    try:
        return {
            "browser": os.environ.get("BROWSER", "ไม่ทราบ"),
            "screen_resolution": shutil.get_terminal_size(),
        }
    except Exception:
        return {"browser": "ไม่ทราบ", "screen_resolution": "ไม่ทราบ"}

# ฟังก์ชันดึงข้อมูลแบตเตอรี่
def get_battery_status():
    try:
        battery = psutil.sensors_battery()
        return {
            "percent": battery.percent,
            "charging": battery.power_plugged,
        }
    except Exception:
        return {"percent": "ไม่ทราบ", "charging": "ไม่ทราบ"}


# ฟังก์ชันดึงข้อมูลการใช้หน่วยความจำ (RAM)
def get_memory_usage():
    try:
        memory = psutil.virtual_memory()
        return {
            "total": f"{round(memory.total / (1024 ** 3), 2)} GB",
            "used": f"{round(memory.used / (1024 ** 3), 2)} GB",
            "free": f"{round(memory.free / (1024 ** 3), 2)} GB",
            "percent": f"{memory.percent}%",
        }
    except Exception:
        return "ไม่สามารถดึงข้อมูลหน่วยความจำ"

# ฟังก์ชันดึงข้อมูลเครือข่าย (Network)
def get_network_info():
    try:
        network = psutil.net_if_addrs()
        return {interface: [addr.address for addr in interfaces if addr.family == socket.AF_INET] for interface, interfaces in network.items()}
    except Exception:
        return "ไม่สามารถดึงข้อมูลเครือข่าย"



# ฟังก์ชันปรับปรุงข้อมูล
def get_full_info():
    ip = get_ip()
    location = get_location(ip)
    device = get_device_info()
    battery = get_battery_status()
    gpu = get_gpu_info()

    memory = get_memory_usage()
    network = get_network_info()

    network2 = get_network_info2()  # ดึงข้อมูลเครือข่าย
    disk = get_disk_usage()  # ดึงข้อมูลการใช้งานดิสก์
    uptime = get_uptime()  # ดึงข้อมูลเวลาการทำงาน

    # ปรับรูปแบบความละเอียดหน้าจอ
    screen_resolution = device.get("screen_resolution")
    if isinstance(screen_resolution, os.terminal_size):
        screen_resolution = f"{screen_resolution.columns} x {screen_resolution.lines}"

    return {
        "IP": ip,
        "Location": location,
        "Device": device,
        "Battery": battery if battery.get("percent") != "ไม่ทราบ" else "ไม่มีข้อมูลแบตเตอรี่",
        "GPU": gpu,
        "Screen Resolution": screen_resolution,

        "Memory": memory,
        "Network": network,

        "Timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    }




