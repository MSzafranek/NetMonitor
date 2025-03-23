import time
import os
import sys
from db_module import save_ping_result, get_ping_stats
from ping_module import ping_addresses

def monitor_network(interval=5):
    """
    Funkcja monitorująca sieć:
    - W nieskończonej pętli pobiera wyniki ping,
    - Wypisuje je na ekranie wraz z aktualnym czasem,
    - Zapisuje wyniki do bazy danych,
    - Czyści ekran przy każdej iteracji.
    """
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} - Wyniki ping:")
            results = ping_addresses()
            for target_name, response_time in results.items():
                print(f"{target_name}: {response_time} ms")
                save_ping_result(target_name, response_time)
            print("\nAby zakończyć monitorowanie, naciśnij CTRL+C.")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitorowanie zakończone. Powrót do menu...")
        time.sleep(2)

def print_stats():
    """
    Funkcja wyświetlająca statystyki ping (średni, min, max) pobrane z bazy danych.
    """
    os.system("cls" if os.name == "nt" else "clear")
    stats = get_ping_stats()
    print("Statystyki ping:")
    for stat in stats:
        print(f"{stat['target']} - Średni: {stat['avg_time']} ms, "
              f"Min: {stat['min_time']} ms, Max: {stat['max_time']} ms")
    input("\nNaciśnij Enter, aby powrócić do menu...")

def cli_menu():
    """
    Proste menu CLI pozwalające wybrać opcję monitorowania lub wyświetlenia statystyk.
    """
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== Monitor sieci ===")
        print("1. Monitoruj sieć (ciągłe zbieranie danych)")
        print("2. Pokaż statystyki ping")
        print("Q. Wyjdź")
        choice = input("Wybierz opcję: ").strip().lower()
        if choice == "1":
            monitor_network()
        elif choice == "2":
            print_stats()
        elif choice == "q":
            print("Zakończenie programu.")
            sys.exit(0)
        else:
            input("Nieprawidłowa opcja. Naciśnij Enter, aby spróbować ponownie.")

if __name__ == "__main__":
    cli_menu()
