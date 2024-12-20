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

# ฟังก์ชันดึงข้อมูล port ของเครือข่าย IP
def get_open_ports():
    open_ports = []
    for conn in psutil.net_connections(kind='inet'):  # ตรวจสอบเฉพาะการเชื่อมต่ออินเทอร์เน็ต
        open_ports.append({
            "laddr": conn.laddr,  # ที่อยู่ไอพีและพอร์ตของเครื่อง
            "raddr": conn.raddr,  # ที่อยู่ไอพีและพอร์ตของเครื่องปลายทาง
            "status": conn.status,  # สถานะการเชื่อมต่อ
            "pid": conn.pid,  # PID ของโปรเซสที่ใช้งานพอร์ตนี้
        })
    return open_ports

# ฟังก์ชันปรับปรุงข้อมูล
def get_full_info():
    ip = get_ip()
    location = get_location(ip)
    device = get_device_info()
    battery = get_battery_status()
    gpu = get_gpu_info()
    open_ports = get_open_ports()

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
        "Open Ports": open_ports,  # เพิ่มข้อมูลพอร์ตที่เปิดใช้งาน
        "Timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    }




