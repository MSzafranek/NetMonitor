import time
from ping_module import ping_addresses
from db_module import save_ping_result, init_db

def monitor_network(interval=60):
    init_db()
    while True:
        results = ping_addresses()
        for target, response_time in results.items():
            save_ping_result(target, response_time)
        time.sleep(interval)

if __name__ == "__main__":
    monitor_network()
