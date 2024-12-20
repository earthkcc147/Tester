import requests
import platform
import ctypes

# ฟังก์ชันดึงข้อมูลเบราว์เซอร์และระบบปฏิบัติการ
def parse_device_details(user_agent):
    if "Windows" in user_agent:
        os = "Windows"
    elif "Macintosh" in user_agent:
        os = "MacOS"
    elif "iPhone" in user_agent:
        os = "iOS"
    elif "Android" in user_agent:
        os = "Android"
    else:
        os = "ไม่ทราบระบบปฏิบัติการ"

    if "Chrome" in user_agent:
        browser = "Google Chrome"
    elif "Firefox" in user_agent:
        browser = "Mozilla Firefox"
    elif "Safari" in user_agent:
        browser = "Safari"
    else:
        browser = "ไม่ทราบเบราว์เซอร์"
    
    return os, browser

# ฟังก์ชันดึงข้อมูลความละเอียดหน้าจอ
def get_screen_resolution():
    try:
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        return f"{screen_width}x{screen_height}"
    except:
        return "ไม่สามารถดึงข้อมูลความละเอียด"

# ฟังก์ชันดึงข้อมูลความเร็วในการเชื่อมต่อ (ประมาณ)
def get_connection_speed():
    try:
        speed_info = requests.get("https://www.speedtest.net/api/js/").json()
        return f"{speed_info['download']} Mbps (ดาวน์โหลด), {speed_info['upload']} Mbps (อัพโหลด)"
    except:
        return "ไม่สามารถดึงข้อมูลความเร็ว"

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

# ฟังก์ชันดึงข้อมูลทั้งหมด
def get_device_info():
    try:
        ip, city, region, country = get_ip_info()
        user_agent = requests.get("https://httpbin.org/user-agent").json().get("user-agent", "ไม่ทราบอุปกรณ์")
        device_model = platform.system()  # สามารถปรับปรุงหากต้องการข้อมูลอุปกรณ์ที่เจาะจงมากขึ้น
        os, browser = parse_device_details(user_agent)
        screen_resolution = get_screen_resolution()
        connection_speed = get_connection_speed()

        return {
            "ip": ip,
            "location": f"{city}, {region}, {country}",
            "device": user_agent,
            "device_model": device_model,
            "os": os,
            "browser": browser,
            "screen_resolution": screen_resolution,
            "connection_speed": connection_speed
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
            "connection_speed": "ไม่สามารถดึงข้อมูล"
        }