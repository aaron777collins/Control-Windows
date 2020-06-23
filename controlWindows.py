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
    pass


def on_release(key):


    if key == keyboard.Key.esc:
        # Stop listener
        return False

    global recording, recText, writeBuffer, instructions
    try:

        if (not recText):
            if (key.char == 'c'):
                instructions.append((pyautogui.position(), "c", ""))
            if (key.char == 'd'):
                instructions.append((pyautogui.position(), "d", ""))
            if (key.char == 'f'):
                instructions.append((pyautogui.position(), "f", ""))
            if (key.char == 's'):
                instructions.append((pyautogui.position(), "s", ""))
            if (key.char == 'a'):
                instructions.append((pyautogui.position(), "a", ""))
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




def recordMovements():
    global instructions, recording, recText, writeBuffer

    recording = True

    while recording:
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
        if (character == 'a'):
            pyautogui.moveTo(location, duration=0.25)
            pyautogui.hotkey('ctrl', 'A')
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

            print("c - click\nd - double click\nf - right click\n` - toggle writing\ns - add waiting time\na - ctrl + A hotkey\ne - end recording")

            dest = os.path.join(os.path.expanduser('~'), 'Desktop\WCScripts', name)

            reader = safe_open(dest, 'wb')
            try:
                recordMovements()
                pickle.dump(instructions, reader)
                print(instructions)
            finally:
                reader.close()


mainCode()
