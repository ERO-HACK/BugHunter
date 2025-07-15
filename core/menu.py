from scanners import xss, lfi, sqli, redirect
from utils.helper import clear_terminal
import time

def main_menu():
    # clear_terminal()
    time.sleep(0.5)
    print("\nSelect an option to start scanning:\n")
    print("1) XSS Scan 🧬")
    print("2) LFI Scan 🗂️")
    print("3) SQL Injection Scan 💉")
    print("4) Redirect Scan 🎯")
    print("0) Exit\n")

    choice = input("Enter your choice (0-4): ").strip()

    if choice == '1':
        target = input("Enter the target URL (e.g., http://example.com/page): ").strip()
        payload_file = "payloads/xss.txt"
        print("\nStarting XSS Scan...\n")
        time.sleep(1)
        xss.xss_scanner(target, payload_file)
    elif choice == '2':
        target = input("Enter the target URL (e.g., http://example.com/page): ").strip()
        payload_file = "payloads/lfi.txt"
        print("\nStarting LFI Scan...\n")
        time.sleep(1)
        lfi.lfi_scanner(target, payload_file)
    elif choice == '3':
        target = input("Enter the target URL (e.g., http://example.com/page): ").strip()
        payload_file = "payloads/sqli.txt"
        print("\nStarting SQL Injection Scan...\n")
        time.sleep(1)
        sqli.sqli_scanner(target, payload_file)
    elif choice == '4':
        target = input("Enter the target URL (e.g., http://example.com/page): ").strip()
        payload_file = "payloads/redirect.txt"
        print("\nStarting Redirect Scan...\n")
        time.sleep(1)
        redirect.redirect_scanner(target, payload_file)
    elif choice == '0':
        print("Exiting... Goodbye!")
        time.sleep(1)
        exit(0)
    else:
        print("Invalid choice! Please select a valid option.")
        time.sleep(2)
        main_menu()
