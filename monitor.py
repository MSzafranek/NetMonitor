import time
from db_module import save_ping_result
from ping_module import ping_addresses

def monitor_network(interval=5):
    while True:
        results = ping_addresses()
        for target_name, response_time in results.items():
            save_ping_result(target_name, response_time)
        # timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        # ping_data = [
        #     {"target": target, "response_time": response_time, "timestamp": timestamp}
        #     for target, response_time in results.items()
        # ]
        time.sleep(interval)
if __name__ == '__main__':
    monitor_network()