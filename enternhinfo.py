import subprocess
import sys
import pyautogui
def install(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])


#Ensures pip is installed:
subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])


install('pyautogui')
install('opencv-python')

pyautogui.moveTo((1442, 379), duration=0.25)
pyautogui.click((1442, 379))
pyautogui.moveTo((1487, 359), duration=0.25)
pyautogui.click((1487, 359))
