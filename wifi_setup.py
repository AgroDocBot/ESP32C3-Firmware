import network
import time

SSID = 'AgriBot'
PASSWORD = 'ilovemaven'

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print(f"Connecting to {SSID}...")
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to WiFi with IP:', wlan.ifconfig()[0])
    return wlan.ifconfig()[0]
