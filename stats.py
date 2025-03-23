from db_module import get_ping_stats

def print_stats():
    stats = get_ping_stats()
    print("Statystyki ping:")
    for stat in stats:
        print(f"{stat['target']} - Avg: {stat['avg_time']} ms, Min: {stat['min_time']} ms, Max: {stat['max_time']} ms")

if __name__ == "__main__":
    print_stats()