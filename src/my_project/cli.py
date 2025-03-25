import os
import sys
import time

from my_project.db_module import get_ping_stats, init_db, save_ping_result
from my_project.ping_module import ping_addresses


def monitor_network(interval: int = 2) -> None:
    """
    Agag.

    Funkcja monitorująca sieć:
    - W nieskończonej pętli pobiera wyniki ping,
    - Wypisuje je na ekranie wraz z aktualnym czasem,
    - Zapisuje wyniki do bazy danych,
    - Czyści ekran przy każdej iteracji.

    :param interval: Częstotliwość zbierania informacji
    """
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'{timestamp} - Wyniki ping:')  # noqa: T201
            results = ping_addresses()
            for target_name, response_time in results.items():
                print(f'{target_name}: {response_time} ms')  # noqa: T201
                save_ping_result(target_name, response_time)
            print('\nAby zakończyć monitorowanie, naciśnij CTRL+C.')  # noqa: T201
            time.sleep(interval)
    except KeyboardInterrupt:
        print('\nMonitorowanie zakończone. Powrót do menu...')  # noqa: T201
        time.sleep(2)


def print_stats() -> None:
    """
    Funkcja wyświetlająca statystyki ping (średni, min, max) pobrane z bazy danych.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605
    stats = get_ping_stats()
    print('Statystyki ping:')  # noqa: T201
    for stat in stats:
        print(  # noqa: T201
            f'{stat["target"]} - Średni: {stat["avg_time"]} ms, '
            f'Min: {stat["min_time"]} ms, Max: {stat["max_time"]} ms',
        )
    input('\nNaciśnij Enter, aby powrócić do menu...')


def cli_menu() -> None:
    """
    Proste menu CLI pozwalające wybrać opcję monitorowania lub wyświetlenia statystyk.
    """
    init_db()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605
        print('=== Monitor sieci ===')  # noqa: T201
        print('1. Monitoruj sieć (ciągłe zbieranie danych)')  # noqa: T201
        print('2. Pokaż statystyki ping')  # noqa: T201
        print('Q. Wyjdź')  # noqa: T201
        choice = input('Wybierz opcję: ').strip().lower()
        if choice == '1':
            monitor_network()
        elif choice == '2':
            print_stats()
        elif choice == 'q':
            print('Zakończenie programu.')  # noqa: T201
            sys.exit(0)
        else:
            input('Nieprawidłowa opcja. Naciśnij Enter, aby spróbować ponownie.')


if __name__ == '__main__':
    cli_menu()
