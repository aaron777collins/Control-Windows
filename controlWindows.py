# Created by Aaron Collins on June 23, 2020
# Used for automating simple tasks on your pc

import errno
import os

import pip
import pyautogui
import pickle
import subprocess
import difflib
import re
from pynput import keyboard

def import_or_install(package):
	try:
		__import__(package)
	except ImportError:
		pip.main(['install', package])

import_or_install('pyautogui')
import_or_install('pyautogui')
import_or_install('pynput')
import_or_install('pynput')
import_or_install('pickle')
import_or_install('pickle')

# pyautogui.PAUSE = 1  # enable to wait 1 second between mouse/keyboard movements/presses
pyautogui.FAILSAFE = True
width, height = pyautogui.size()

recording = False
recText = False
writeBuffer = ""
pic_num = 0
cur_num = -1
pic_initial_point = None
pic_dest = ""


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

    global recording, recText, writeBuffer, instructions, pic_num, cur_num, pic_initial_point
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
            if (key.char == 'x'):
                if(cur_num == pic_num):
                    instructions.append(([pic_initial_point, pyautogui.position()], "x", str(pic_num)))

                    pyautogui.screenshot(pic_dest + str(pic_num) + ".png", region=(pic_initial_point.x, pic_initial_point.y, abs(pyautogui.position().x - pic_initial_point.x), abs(pyautogui.position().y - pic_initial_point.y)))



                    pic_num += 1
                    cur_num = -1
                    pic_initial_point = None
                else:
                    cur_num = pic_num
                    pic_initial_point = pyautogui.position()
            if (key.char == 'e'):
                instructions.append((pyautogui.position(), "end", ""))
                recording = False
                cur_num = -1
                pic_num = 0
                pic_initial_point = None
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

    if (key == keyboard.Key.enter and recording and len(instructions) > 0):
        instructions.append((pyautogui.position(), 'enter', ""))


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

instructions = []




def recordMovements():
    global instructions, recording, recText, writeBuffer

    recording = True

    instructions = None
    instructions = []

    while recording:
        pass
    recText = False
    writeBuffer = None

# old function used for executing old files
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
            pyautogui.hotkey('ctrl', 'a')
        if (character == 'enter'):
            pyautogui.moveTo(location, duration=0.25)
            pyautogui.press('enter')
        if (character == 'end'):
            break


def mainCode():
    global instructions, pic_dest

    print("NOTE: input is responsive until esc is pressed")

    action = None

    while (action != 'e' or action != 'exit'):

        action = input("Enter r to record an action sequence\nEnter q to run an action sequence\nEnter t to convert an old script to a new one\nEnter 'e' to exit:\n")

        instructions = None
        instructions = []

        if (action == 'e' or action == 'exit'):
            break;

        if (action == 'q'):
            name = input("Enter the file name (exclude extension type)\n")
            rawName = name
            name = name + ".py"

            destFolder = os.path.join(os.path.expanduser('~'), "Desktop\WCScripts")
            dest = os.path.join(os.path.expanduser('~'), "Desktop\WCScripts", name)

            reTry = True

            while reTry:
                try:
                    # will create the directory if necessary
                    reader = safe_open(dest, 'rb')

                    reader.close()


                    cmd = 'python ' + "\"" + dest + "\""

                    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                    out, err = p.communicate()
                    result = out.decode().split('\n')
                    for lin in result:
                        if not lin.startswith('#'):
                            print(lin)
                    reTry = False

                except FileNotFoundError:
                    print("ERROR: file {0} not found!".format(name))

                    fileArr = []

                    for root, dirs, files in os.walk(destFolder):
                        for file in files:
                            if file.endswith(".py"):
                                # print(file)
                                fileArr.append(file)

                    closestMatches = difflib.get_close_matches(rawName, fileArr, cutoff=0.4, n=5)

                    if(len(closestMatches) > 0):
                        print("Similar file names were found:")
                        nameNum = 1
                        for match in closestMatches:
                            print(str(nameNum) + " - " + match)
                            nameNum += 1

                        runAgain = input("Would you like to try one of these files? (y/n):\n")
                        if(runAgain == "y" or runAgain == "yes"):
                            reTry = True
                            selected_num = int(input("Which file would you like to run? (enter the id):\n"))

                            # resetting the variables to account for the new name
                            name = closestMatches[selected_num-1].rsplit('.', 1)[0]
                            rawName = name
                            name = name + ".py"

                            destFolder = os.path.join(os.path.expanduser('~'), "Desktop\WCScripts")
                            dest = os.path.join(os.path.expanduser('~'), "Desktop\WCScripts", name)

                        else:
                            reTry = False
                    else:
                        reTry = False





        if (action == 't'):
            name_orig = input("Enter the old file name (exclude extension type)\n")
            name = name_orig + ".aseq"

            destFolder = os.path.join(os.path.expanduser('~'), "Desktop\WCScripts")
            dest = os.path.join(os.path.expanduser('~'), "Desktop\WCScripts", name)

            reTry = True

            while reTry:

                try:
                    reader = safe_open(dest, 'rb')
                    try:
                        instructions = pickle.load(reader)

                        name2 = name_orig + ".py"

                        dest2 = os.path.join(os.path.expanduser('~'), 'Desktop\WCScripts', name2)

                        reader2 = safe_open(dest2, 'w')
                        try:
                            # using python script to make human readible instead now
                            reader2.write("import pip\n")
                            reader2.write("import pyautogui\n\n")
                            reader2.write("def import_or_install(package):\n")
                            reader2.write("\ttry:\n")
                            reader2.write("\t\t__import__(package)\n")
                            reader2.write("\texcept ImportError:\n")
                            reader2.write("\t\tpip.main(['install', package])\n")
                            reader2.write("\n\nimport_or_install('pyautogui')")
                            reader2.write("\nimport_or_install('pyautogui')\n\n")
                            for location, character, writeBufferLocal in instructions:

                                if (character == 'c'):
                                    reader2.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[
                                        1]) + ", duration=0.25)\n")
                                    reader2.write("pyautogui.click(" + "({0}, {1})".format(location[0], location[1]) + ")\n")
                                if (character == 'd'):
                                    reader2.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[
                                        1]) + ", duration=0.25)\n")
                                    reader2.write("pyautogui.doubleClick(" + "({0}, {1})".format(location[0], location[
                                        1]) + ", duration=0.1)\n")
                                if (character == 'f'):
                                    reader2.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[
                                        1]) + ", duration=0.25)\n")
                                    reader2.write(
                                        "pyautogui.rightClick(" + "({0}, {1})".format(location[0], location[1]) + ")\n")
                                if (character == 's'):  # used for adding buffer time
                                    reader2.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[
                                        1]) + ", duration=2.0)\n")
                                if (character == 'w'):
                                    reader2.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[
                                        1]) + ", duration=0.25)\n")
                                    reader2.write("pyautogui.write(\'" + writeBufferLocal + "\', interval=0.05)\n")
                                if (character == 'a'):
                                    reader2.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[
                                        1]) + ", duration=0.25)\n")
                                    reader2.write("pyautogui.hotkey('ctrl', 'a')\n")
                                if (character == 'enter'):
                                    reader2.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[
                                        1]) + ", duration=0.25)\n")
                                    reader2.write("pyautogui.press('enter')\n")
                                if (character == 'end'):
                                    break

                            print(instructions)
                        finally:
                            reader2.close()


                    finally:
                        reader.close()
                        reTry = False

                except FileNotFoundError:
                    print("ERROR: file {0} not found!".format(name))

                    fileArr = []

                    for root, dirs, files in os.walk(destFolder):
                        for file in files:
                            if file.endswith(".aseq"):
                                # print(file)
                                fileArr.append(file)

                    closestMatches = difflib.get_close_matches(name_orig, fileArr, cutoff=0.4, n=5)

                    if (len(closestMatches) > 0):
                        print("Similar file names were found:")
                        nameNum = 1
                        for match in closestMatches:
                            print(str(nameNum) + " - " + match)
                            nameNum += 1

                        runAgain = input("Would you like to convert one of these? (y/n):\n")
                        if (runAgain == "y" or runAgain == "yes"):
                            reTry = True
                            selected_num = int(input("Which file would you like to convert? (enter the id):\n"))

                            # resetting the variables to account for the new name
                            name_orig = closestMatches[selected_num - 1].rsplit('.', 1)[0]
                            name = name_orig + ".aseq"

                            dest = os.path.join(os.path.expanduser('~'), "Desktop\WCScripts", name)

                        else:
                            reTry = False
                    else:
                        reTry = False

        if (action == 'r'):
            name = input("Enter the file name (exclude extension type)\n")
            rawName = name
            name = name + ".py"

            print("c - click\nd - double click\nf - right click\n` - toggle writing\ns - add waiting time\na - ctrl + A hotkey\nx - press twice, once for the top left of the\nobject and once for the bottom right of the object\nThe program will later find this object and click the center\ne - end recording")

            dest = os.path.join(os.path.expanduser('~'), 'Desktop\WCScripts', name)

            pic_dest = os.path.join(os.path.expanduser('~'), "Desktop\WCScripts", rawName)

            reader = safe_open(dest, 'w')
            try:
                recordMovements()
                # pickle.dump(instructions, reader)
                # using python script to make human readible instead now
                reader.write("import pip\n")
                reader.write("import pyautogui\n")
                reader.write("def import_or_install(package):\n")
                reader.write("\ttry:\n")
                reader.write("\t\t__import__(package)\n")
                reader.write("\texcept ImportError:\n")
                reader.write("\t\tpip.main(['install', package])\n")
                reader.write("\n\nimport_or_install('pyautogui')")
                reader.write("\nimport_or_install('pyautogui')\n\n")
                reader.write("\nimport_or_install('opencv-python')\n\n")
                for location, character, writeBufferLocal in instructions:

                    if (character == 'c'):
                        reader.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) +", duration=0.25)\n")
                        reader.write("pyautogui.click(" + "({0}, {1})".format(location[0], location[1]) +")\n")
                    if (character == 'd'):
                        reader.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) +", duration=0.25)\n")
                        reader.write("pyautogui.doubleClick(" + "({0}, {1})".format(location[0], location[1]) +", duration=0.1)\n")
                    if (character == 'f'):
                        reader.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) +", duration=0.25)\n")
                        reader.write("pyautogui.rightClick(" + "({0}, {1})".format(location[0], location[1]) +")\n")
                    if (character == 's'):  # used for adding buffer time
                        reader.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) +", duration=2.0)\n")
                    if (character == 'w'):
                        reader.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) +", duration=0.25)\n")
                        reader.write("pyautogui.write(\'" + writeBufferLocal + "\', interval=0.05)\n")
                    if (character == 'a'):
                        reader.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) +", duration=0.25)\n")
                        reader.write("pyautogui.hotkey('ctrl', 'a')\n")
                    if (character == 'x'):
                        reader.write("x, y = pyautogui.locateCenterOnScreen('" + re.escape(pic_dest + writeBufferLocal) + ".png" + "', confidence=0.8)\n")
                        reader.write("pyautogui.moveTo( (x, y), duration=0.25)\n")
                        reader.write("pyautogui.click((x, y))\n")
                    if (character == 'enter'):
                        reader.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) +", duration=0.25)\n")
                        reader.write("pyautogui.press('enter')\n")
                    if (character == 'end'):
                        break

                print(instructions)
            finally:
                reader.close()


mainCode()
