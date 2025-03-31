from db_module import get_ping_stats


def print_stats() -> None:
    """
    _summary_.
    """
    stats = get_ping_stats()
    for _stat in stats:
        pass


if __name__ == '__main__':
    print_stats()
