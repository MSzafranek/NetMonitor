from ping3 import ping


def ping_addresses() -> dict[str, int]:
    """
    _summary_.

    :return: _description_
    """
    targets = {'internet': '8.8.8.8', 'gateway': '192.168.0.1'}
    results = {}
    for target_name, address in targets.items():
        response_time = round(ping(address) * 1000)
        results[target_name] = response_time if response_time is not None else -1
    return results


if __name__ == '__main__':
    pass
