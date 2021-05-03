import subprocess
import ensurepip
from sys import platform
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def checkLinux():
    return platform == "linux" or platform == "linux2"


def installAll():
    # ensuring pip is installed

    if checkLinux():
        subprocess.check_call(["sudo", "apt-get", "install", "python3-pip"])
    else:
        ensurepip.bootstrap()

    install("pynput")

    install("pyautogui")

    install("pickle-mixin")

    print("\n\n########################################\nAll Dependencies Installed.\n")
