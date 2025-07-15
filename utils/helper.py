import os
import platform

def clear_terminal():
    """پاک کردن ترمینال برای ویندوز و لینوکس/macOS"""
    command = "cls" if platform.system() == "Windows" else "clear"
    os.system(command)
