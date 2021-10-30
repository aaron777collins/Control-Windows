import subprocess
import sys
import pyautogui
def install(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])


#Ensures pip is installed:
subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])


install('pyautogui')
install('opencv-python')

pyautogui.moveTo((1086, 182), duration=0.25)
pyautogui.click((1086, 182))
pyautogui.moveTo((972, 395), duration=2.0)
pyautogui.dragTo((1524, 880), duration=0.25, button='left')
pyautogui.moveTo((1432, 660), duration=0.25)
pyautogui.hotkey('ctrl', 'c')
pyautogui.moveTo((275, 1064), duration=0.25)
pyautogui.click((275, 1064))
pyautogui.moveTo((275, 1064), duration=0.25)
pyautogui.write('notepad', interval=0.05)
pyautogui.moveTo((275, 1064), duration=0.25)
pyautogui.press('enter')
pyautogui.moveTo((774, 552), duration=0.25)
pyautogui.click((774, 552))
pyautogui.moveTo((774, 552), duration=0.25)
pyautogui.hotkey('ctrl', 'v')
