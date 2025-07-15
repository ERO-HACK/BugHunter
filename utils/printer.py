from termcolor import colored

def print_colored(text, color="white"):
    colors = ["red", "green", "yellow", "cyan", "magenta", "white"]
    if color not in colors:
        color = "white"
    print(colored(text, color))

def print_success(url, payload, status_code):
    print(colored(f"[VULNERABLE] {url} | Payload: {payload} | Status: {status_code}", "green", attrs=["bold"]))

def print_failure(url, payload, status_code):
    print(colored(f"[NOT VULNERABLE] {url} | Payload: {payload} | Status: {status_code}", "red"))
