import time

from db_module import save_ping_result
from ping_module import ping_addresses


def monitor_network(interval: int = 5) -> None:
    """
    _summary_.

    :param interval: _description_, defaults to 5
    """
    while True:
        results = ping_addresses()
        for target_name, response_time in results.items():
            save_ping_result(target_name, response_time)
        time.sleep(interval)


if __name__ == '__main__':
    monitor_network()
