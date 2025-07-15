from core.cli import show_help
from core.menu import main_menu
from utils.baneerr import animated_banner
from utils.helper import clear_terminal

import sys

def main():
    clear_terminal()

    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        show_help()
    else:
        animated_banner()
        main_menu()

if __name__ == '__main__':
    main()
