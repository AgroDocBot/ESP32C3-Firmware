from wifi_setup import connect_to_wifi
from web_server_ws import start_server_ws
import uasyncio as asyncio

async def main():
    ip_address = connect_to_wifi()
    print(f"Server IP address: {ip_address}")
    await start_server_ws()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Server stopped")

