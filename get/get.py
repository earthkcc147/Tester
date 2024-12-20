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

# ฟังก์ชันดึงข้อมูล port ที่ใช้งาน
def get_active_ports():
    try:
        active_ports = []
        for conn in psutil.net_connections(kind="inet"):
            if conn.laddr and conn.status == "LISTEN":
                active_ports.append(conn.laddr.port)
        return active_ports if active_ports else "ไม่มี port ที่เปิดใช้งาน"
    except Exception:
        return "ไม่สามารถดึงข้อมูล port ได้"

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

# ฟังก์ชันปรับปรุงข้อมูล
def get_full_info():
    ip = get_ip()
    ports = get_active_ports()
    location = get_location(ip)
    device = get_device_info()
    battery = get_battery_status()
    gpu = get_gpu_info()

    # ปรับรูปแบบความละเอียดหน้าจอ
    screen_resolution = device.get("screen_resolution")
    if isinstance(screen_resolution, os.terminal_size):
        screen_resolution = f"{screen_resolution.columns} x {screen_resolution.lines}"

    return {
        "IP": ip,
        "Ports": ports,
        "Location": location,
        "Device": device,
        "Battery": battery if battery.get("percent") != "ไม่ทราบ" else "ไม่มีข้อมูลแบตเตอรี่",
        "GPU": gpu,
        "Screen Resolution": screen_resolution,
        "Timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    }