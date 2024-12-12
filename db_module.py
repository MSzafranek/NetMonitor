import sqlite3

def init_db():
    # Połączenie z bazą danych (tworzy ją, jeśli nie istnieje)
    conn = sqlite3.connect("network_monitor.db")
    c = conn.cursor()

    # Tworzenie tabeli 'pings', jeśli nie istnieje
    c.execute("""
        CREATE TABLE IF NOT EXISTS pings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            response_time REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()  # Zatwierdzenie zmian w bazie
    conn.close()   # Zamknięcie połączenia


import sqlite3

def save_ping_result(target, response_time):
    conn = sqlite3.connect("network_monitor.db")
    c = conn.cursor()
    c.execute("INSERT INTO pings (target, response_time) VALUES (?, ?)", (target, response_time))
    conn.commit()
    conn.close()




def get_ping_stats():
    conn = sqlite3.connect("network_monitor.db")
    c = conn.cursor()
    c.execute("""
        SELECT target, AVG(response_time) AS avg_time, 
               MIN(response_time) AS min_time, 
               MAX(response_time) AS max_time 
        FROM pings GROUP BY target
    """)
    data = c.fetchall()
    conn.close()
    return [{"target": row[0], "avg_time": row[1], "min_time": row[2], "max_time": row[3]} for row in data]
