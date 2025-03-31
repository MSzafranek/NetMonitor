import time

from my_project.db_module import save_ping_result
from my_project.ping_module import ping_addresses


def monitor_network(interval: int = 5) -> None:
    """
    Monitoruj sieć i zapisuj wyniki ping do bazy danych.

    :param interval: co ile sekund wykonywać ping
    """
    while True:
        results = ping_addresses()
        for target_name, response_time in results.items():
            save_ping_result(target_name, response_time)
        time.sleep(interval)


if __name__ == '__main__':
    monitor_network()
