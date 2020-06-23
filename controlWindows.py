# Created by Aaron Collins on June 23, 2020
# Used for automating simple tasks on your pc

import errno
import os
import pyautogui
import pickle
from pynput import keyboard

# pyautogui.PAUSE = 1  # enable to wait 1 second between mouse/keyboard movements/presses
pyautogui.FAILSAFE = True
width, height = pyautogui.size()

C_PRESSED = False
D_PRESSED = False
F_PRESSED = False
S_PRESSED = False

recording = False
recText = False
writeBuffer = ""


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def safe_open(path, openType):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    mkdir_p(os.path.dirname(path))
    return open(path, openType)


def on_press(key):
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    global C_PRESSED, D_PRESSED, F_PRESSED, S_PRESSED
    try:
        if (key.char == 'c'):
            C_PRESSED = True
        if (key.char == 'd'):
            D_PRESSED = True
        if (key.char == 'f'):
            F_PRESSED = True
        if (key.char == 's'):
            S_PRESSED = True
    except AttributeError:
        pass


def on_release(key):


    if key == keyboard.Key.esc:
        # Stop listener
        return False

    global C_PRESSED, D_PRESSED, F_PRESSED, S_PRESSED, recording, recText, writeBuffer, instructions
    try:

        if (not recText):
            if (key.char == 'c'):
                C_PRESSED = False
            if (key.char == 'd'):
                D_PRESSED = False
            if (key.char == 'f'):
                F_PRESSED = False
            if (key.char == 's'):
                S_PRESSED = False
            if (key.char == 'e'):
                recording = False
        else:
            if(key.char != '`'):
                if(writeBuffer != None):
                    writeBuffer = writeBuffer + str(key.char)
                else:
                    writeBuffer = "" + str(key.char)
        if (key.char == '`'):
            if (not recText):
                recText = True
            else:
                recText = False
                instructions.append((pyautogui.position(), "w", writeBuffer))
                writeBuffer = None


    except AttributeError:
        pass

    if (key == keyboard.Key.space and recText):
        if (writeBuffer != None):
            writeBuffer = writeBuffer + " "
        else:
            writeBuffer = " "

    if (key == keyboard.Key.backspace and recText):
        if (writeBuffer != None):
            writeBuffer = writeBuffer[0:-1]
        else:
            writeBuffer = ""

    if (key == keyboard.Key.enter and recording):
        instructions.append((pyautogui.position(), 'enter', ""))


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

instructions = []


def recordingKeyPressed():
    global C_PRESSED, D_PRESSED, F_PRESSED, S_PRESSED
    return C_PRESSED or D_PRESSED or F_PRESSED or S_PRESSED


def getCurAction():
    global C_PRESSED, D_PRESSED, F_PRESSED, S_PRESSED
    if (D_PRESSED):
        return 'd'
    if (C_PRESSED):
        return 'c'
    if (F_PRESSED):
        return 'f'
    if (S_PRESSED):
        return 's'

def recordMovements():
    global instructions, recording, C_PRESSED, D_PRESSED, S_PRESSED, recText, writeBuffer

    recording = True

    while recording:
        if (recordingKeyPressed()):
            instructions.append((pyautogui.position(), getCurAction(), ""))
            while (recordingKeyPressed()):
                pass
    recText = False
    writeBuffer = None


def execMovements():
    global instructions
    for location, character, writeBufferLocal in instructions:
        print(location, character)
        if (character == 'c'):
            pyautogui.moveTo(location, duration=0.25)
            pyautogui.click(location)
        if (character == 'd'):
            pyautogui.moveTo(location, duration=0.25)
            pyautogui.doubleClick(location, duration=0.1)
        if (character == 'f'):
            pyautogui.moveTo(location, duration=0.25)
            pyautogui.rightClick(location)
        if (character == 's'): #used for adding buffer time
            pyautogui.moveTo(location, duration=2.0)
        if (character == 'w'):
            pyautogui.moveTo(location, duration=0.25)
            pyautogui.write(writeBufferLocal, interval=0.05)
        if (character == 'enter'):
            pyautogui.moveTo(location, duration=0.25)
            pyautogui.press('enter')


def mainCode():
    global instructions

    print("NOTE: input is responsive until esc is pressed")

    action = None

    while (action != 'e' or action != 'exit'):

        action = input("Enter r to record an action sequence\nEnter q to run an action sequence\nEnter 'e' to exit:\n")

        instructions = []

        if (action == 'e' or action == 'exit'):
            break;

        if (action == 'q'):
            name = input("Enter the file name (exclude extension type)\n")
            name = name + ".aseq"

            dest = os.path.join(os.path.expanduser('~'), 'Desktop\WCScripts', name)

            try:
                reader = safe_open(dest, 'rb')
                try:
                    instructions = pickle.load(reader)
                finally:
                    reader.close()
                execMovements()
            except FileNotFoundError:
                print("ERROR: file {0} not found!".format(name))

        if (action == 'r'):
            name = input("Enter the file name (exclude extension type)\n")
            name = name + ".aseq"

            print("c - click\nd - double click\nf - right click\n` - toggle writing\ns - add waiting time\ne - end recording")

            dest = os.path.join(os.path.expanduser('~'), 'Desktop\WCScripts', name)

            reader = safe_open(dest, 'wb')
            try:
                recordMovements()
                pickle.dump(instructions, reader)
                print(instructions)
            finally:
                reader.close()


mainCode()
