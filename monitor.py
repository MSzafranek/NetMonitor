import time
from ping_module import ping_addresses

def monitor_network(interval=60):
    while True:
        ping_addresses()
        time.sleep(interval)
