import requests
from utils.printer import print_success, print_failure
from utils.timer import show_timer
import time

def xss_scanner(target_url, payload_file):
    print(f"Starting XSS scan on {target_url}")
    try:
        with open(payload_file, "r") as f:
            payloads = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Payload file {payload_file} not found!")
        return

    total = len(payloads)
    show_timer(total, "XSS Scan")

    for payload in payloads:
        # Pause a bit to simulate timing difference
        time.sleep(0.3)
        test_url = f"{target_url}?q={payload}"
        try:
            response = requests.get(test_url, timeout=10)
            status = response.status_code
            content = response.text
            if payload in content:
                print_success(test_url, payload, status)
            else:
                print_failure(test_url, payload, status)
        except requests.RequestException as e:
            print(f"Request error: {e}")
