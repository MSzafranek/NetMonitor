from ping3 import ping

def ping_addresses():
    targets = {"internet": "8.8.8.8", "gateway": " 192.168.0.1"}
    results = {}

    for target_name, address in targets.items():
        response_time = ping(address)
        results[target_name] = response_time if response_time is not None else -1

    return results
