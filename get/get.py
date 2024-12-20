import os
import platform
import socket
import psutil
import requests
from user_agents import parse

def get_device_info():
    # ตรวจสอบ IP Address
    ip = requests.get('https://api.ipify.org').text
    
    # ตรวจสอบตำแหน่งที่อยู่ (สามารถใช้ IP Geolocation API)
    location = requests.get(f'https://ipinfo.io/{ip}/json').json()
    city = location.get('city', 'ไม่ทราบ')
    region = location.get('region', 'ไม่ทราบ')
    country = location.get('country', 'ไม่ทราบ')

    # ตรวจสอบข้อมูลอุปกรณ์
    user_agent = os.environ.get('HTTP_USER_AGENT', 'ไม่ทราบ')
    device_info = parse(user_agent)

    # ระบบปฏิบัติการ
    os_name = platform.system()  # เช่น Windows, Linux, macOS
    os_version = platform.version()  # เวอร์ชันของระบบปฏิบัติการ

    # ข้อมูลฮาร์ดแวร์
    cpu = psutil.cpu_percent(interval=1)  # ความเร็วในการใช้งาน CPU
    ram = psutil.virtual_memory().percent  # ความจำที่ใช้งาน
    battery = psutil.sensors_battery().percent if psutil.sensors_battery() else 'ไม่สามารถดึงข้อมูลแบตเตอรี่'

    # ข้อมูลเบราว์เซอร์
    browser = device_info.browser.family
    device_type = device_info.device.family
    model = device_info.device.model
    screen_resolution = os.environ.get('SCREEN_RESOLUTION', 'ไม่ทราบ')  # สมมุติว่าให้ใช้การตั้งค่า SCREEN_RESOLUTION

    # ส่งคืนข้อมูลทั้งหมด
    return {
        'ip': ip,
        'location': f"{city}, {region}, {country}",
        'os': os_name,
        'os_version': os_version,
        'cpu': cpu,
        'ram': ram,
        'battery': battery,
        'browser': browser,
        'device_type': device_type,
        'model': model,
        'screen_resolution': screen_resolution
    }