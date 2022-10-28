import os
import time

from lib.utils import logger


# Find the saved wifi networks
def get_saved_wifi_networks():
    saved_networks = []
    for line in os.popen('netsh wlan show profiles'):
        if 'All User Profile' in line:
            saved_networks.append(line.split(':')[1].strip())
    return saved_networks


# Get current 192.168.1.x
def get_current_wireless_ip():
    is_found = False
    for line in os.popen('ipconfig'):
        if 'Wireless LAN adapter Wi-Fi' in line:
            is_found = True
        if is_found and 'IPv4 Address' in line:
            return line.split(':')[1].strip()


# Check user actively connected to wifi
current_ip = get_current_wireless_ip()
if current_ip is None:
    logger('No active wifi connection', 'error')
    saved_wifis = get_saved_wifi_networks()
    if len(saved_wifis) == 0:
        logger('No saved wifi networks', 'error')
        exit(13)
    else:
        logger(f'Forcing connection to {saved_wifis[0]}')
        os.system(f'netsh wlan connect name="{saved_wifis[0]}"')

        logger('Waiting 5 seconds for connection to be established', 'warning')
        # Wait 5 seconds for connection to be established
        time.sleep(5)

        current_ip = get_current_wireless_ip()
        if current_ip is None:
            logger('Failed to connect to wifi', 'error')
            exit(14)
else:
    logger(f'Socket will start on {current_ip}')
