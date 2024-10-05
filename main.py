from wifi_setup import connect_to_wifi
from web_server import start_server

def main():
    ip_address = connect_to_wifi()
    print(f"Server IP address: {ip_address}")
    start_server()

main()
