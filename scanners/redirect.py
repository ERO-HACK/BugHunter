import requests
from utils.printer import print_success, print_failure
from utils.timer import show_timer
import time

def redirect_scanner(target_url, payload_file):
    print(f"Starting Redirect scan on {target_url}")
    try:
        with open(payload_file, "r") as f:
            payloads = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Payload file {payload_file} not found!")
        return

    total = len(payloads)
    show_timer(total, "Redirect Scan")

    for payload in payloads:
        time.sleep(0.3)
        test_url = f"{target_url}?url={payload}"
        try:
            response = requests.get(test_url, allow_redirects=False, timeout=10)
            status = response.status_code
            location = response.headers.get("Location", "")
            if status in [301, 302, 303, 307, 308] and payload in location:
                print_success(test_url, payload, status)
            else:
                print_failure(test_url, payload, status)
        except requests.RequestException as e:
            print(f"Request error: {e}")
