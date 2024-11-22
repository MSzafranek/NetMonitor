import sqlite3

conn = sqlite3.connect("network_monitor.db")
c = conn.cursor()

# Sprawdź, czy tabela istnieje
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pings';")
result = c.fetchone()
if result:
    print("Tabela pings istnieje.")
else:
    print("Tabela pings nie istnieje.")

conn.close()
