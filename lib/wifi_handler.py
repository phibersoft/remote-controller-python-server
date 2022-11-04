import os
import time

from lib.utils import logger


# Get wifi networks
def get_wifi_networks():
    networks = []
    for line in os.popen('netsh wlan show networks'):
        if 'SSID' in line:
            networks.append(line.split(':')[1].strip())
    return networks


# Find the saved wifi networks
def get_saved_active_wifi_networks():
    networks = get_wifi_networks()
    saved_networks = []
    for line in os.popen('netsh wlan show profiles'):
        if 'All User Profile' in line:
            saved_network = line.split(':')[1].strip()
            if saved_network in networks:
                saved_networks.append(saved_network)
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
    saved_wifis = get_saved_active_wifi_networks()
    if len(saved_wifis) == 0:
        logger('No saved active wifi networks', 'error')
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

logger(f'Socket server will be available at http://{current_ip}:9292')
