# Created by Aaron Collins on June 23, 2020
# Used for automating simple tasks on your pc

import dependencies as dependencies
dependencies.installAll()

import errno
import os

import pyautogui
import pickle
import subprocess
import difflib
import re
import subprocess
import sys
from pynput import keyboard
from Utilities import Utilities

# pyautogui.PAUSE = 1  # enable to wait 1 second between mouse/keyboard movements/presses
pyautogui.FAILSAFE = True

class Controller:

    width, height = pyautogui.size()

    recording = False
    recText = False
    writeBuffer = ""
    pic_num = 0
    cur_num = -1
    pic_initial_point = None
    FILE_FOLDER = os.getcwd()
    pic_dest = os.path.join(FILE_FOLDER, "images")
    removingBackTick = False

    listener = None
    instructions = []

    def on_press(self, key):
        # try:
        #     print('alphanumeric key {0} pressed'.format(
        #         key.char))
        # except AttributeError:
        #     print('special key {0} pressed'.format(
        #         key))
        pass

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False

        try:

            if (not self.recText and self.recording):
                if (key.char == 'c'):
                    self.instructions.append((pyautogui.position(), "c", ""))
                    print((pyautogui.position(), "c", ""))
                    pyautogui.press("backspace")
                if (key.char == 'd'):
                    self.instructions.append((pyautogui.position(), "d", ""))
                    print((pyautogui.position(), "d", ""))
                    pyautogui.press("backspace")
                if (key.char == 'f'):
                    self.instructions.append((pyautogui.position(), "f", ""))
                    print((pyautogui.position(), "f", ""))
                    pyautogui.press("backspace")
                if (key.char == 's'):
                    self.instructions.append((pyautogui.position(), "s", ""))
                    print((pyautogui.position(), "s", ""))
                    pyautogui.press("backspace")
                if (key.char == 'l'):
                    self.instructions.append((pyautogui.position(), "l", ""))
                    print((pyautogui.position(), "l", ""))
                    pyautogui.press("backspace")
                if (key.char == 'a'):
                    self.instructions.append((pyautogui.position(), "a", ""))
                    print((pyautogui.position(), "a", ""))
                    pyautogui.press("backspace")
                if (key.char == 'o'):
                    self.instructions.append((pyautogui.position(), "o", ""))
                    print((pyautogui.position(), "o", ""))
                    pyautogui.press("backspace")
                if (key.char == 'p'):
                    self.instructions.append((pyautogui.position(), "p", ""))
                    print((pyautogui.position(), "p", ""))
                    pyautogui.press("backspace")
                if (key.char == 'i'):
                    self.instructions.append((pyautogui.position(), "i", ""))
                    print((pyautogui.position(), "i", ""))
                    pyautogui.press("backspace")
                if (key.char == 'x'):
                    if (self.cur_num == self.pic_num):
                        self.instructions.append(([self.pic_initial_point, pyautogui.position()], "x", str(self.pic_num)))

                        pyautogui.screenshot(self.pic_dest + str(self.pic_num) + ".png", region=(
                            self.pic_initial_point.x, self.pic_initial_point.y, abs(pyautogui.position().x - self.pic_initial_point.x),
                            abs(pyautogui.position().y - self.pic_initial_point.y)))

                        self.pic_num += 1
                        self.cur_num = -1
                        print(([self.pic_initial_point, pyautogui.position()], "x", str(self.pic_num)))
                        self.pic_initial_point = None
                    else:
                        self.cur_num = self.pic_num
                        self.pic_initial_point = pyautogui.position()
                        print((self.pic_initial_point, "x", self.cur_num))
                    pyautogui.press("backspace")
                if (key.char == 'z'):
                    if (self.cur_num == self.pic_num):
                        self.instructions.append(([self.pic_initial_point, pyautogui.position()], "z", str(self.pic_num)))

                        pyautogui.screenshot(self.pic_dest + str(self.pic_num) + ".png", region=(
                            self.pic_initial_point.x, self.pic_initial_point.y, abs(pyautogui.position().x - self.pic_initial_point.x),
                            abs(pyautogui.position().y - self.pic_initial_point.y)))

                        self.pic_num += 1
                        self.cur_num = -1
                        print(([self.pic_initial_point, pyautogui.position()], "z", str(self.pic_num)))
                        self.pic_initial_point = None
                    else:
                        self.cur_num = self.pic_num
                        self.pic_initial_point = pyautogui.position()
                        print((self.pic_initial_point, "z", self.cur_num))
                    pyautogui.press("backspace")
                if (key.char == 'u'):
                    if (self.cur_num == self.pic_num):
                        self.instructions.append(([self.pic_initial_point, pyautogui.position()], "u", str(self.pic_num)))

                        pyautogui.screenshot(self.pic_dest + str(self.pic_num) + ".png", region=(
                            self.pic_initial_point.x, self.pic_initial_point.y, abs(pyautogui.position().x - self.pic_initial_point.x),
                            abs(pyautogui.position().y - self.pic_initial_point.y)))

                        self.pic_num += 1
                        self.cur_num = -1
                        print(([self.pic_initial_point, pyautogui.position()], "u", str(self.pic_num)))
                        self.pic_initial_point = None
                    else:
                        self.cur_num = self.pic_num
                        self.pic_initial_point = pyautogui.position()
                        print((self.pic_initial_point, "u", self.cur_num))
                    pyautogui.press("backspace")
                if (key.char == 'e'):
                    self.instructions.append((pyautogui.position(), "end", ""))
                    self.recording = False
                    self.cur_num = -1
                    self.pic_num = 0
                    self.pic_initial_point = None
                    pyautogui.press("backspace")
            else:
                if (self.recording):
                    if (self.writeBuffer != None):
                        self.writeBuffer = self.writeBuffer + str(key.char)
                    else:
                        self.writeBuffer = "" + str(key.char)
            if (key.char == '`' and self.recording):
                self.removingBackTick = True
                pyautogui.press("backspace")
                if (not self.recText):
                    self.recText = True
                    print("Writing Mode Enabled. Anything you type will be recorded..")
                else:
                    self.recText = False
                    if (self.writeBuffer != None):  # removing backtick
                        self.writeBuffer = self.writeBuffer[0:-1]
                    else:
                        self.writeBuffer = ""
                    self.instructions.append((pyautogui.position(), "w", self.writeBuffer))
                    print("Writing Mode Disabled. You recorded: \'" + self.writeBuffer + "\'")
                    self.writeBuffer = None




        except AttributeError:
            pass

        if (key == keyboard.Key.space and self.recText and self.recording):
            if (self.writeBuffer != None):
                self.writeBuffer = self.writeBuffer + " "
            else:
                self.writeBuffer = " "

        if (key == keyboard.Key.backspace and self.recText and self.recording):
            if (self.writeBuffer != None):
                self.writeBuffer = self.writeBuffer[0:-1]
            else:
                self.writeBuffer = ""
            if not self.removingBackTick:
                print("Backspace detected! Your write buffer now says: \'" + self.writeBuffer + "\'")
            else:
                self.removingBackTick = False

        if (key == keyboard.Key.enter and self.recording and not self.recText and len(self.instructions) > 0):
            self.instructions.append((pyautogui.position(), 'enter', ""))
            print((pyautogui.position(), 'enter', ""))

    def recordMovements(self):

        self.recording = True

        self.instructions = None
        self.instructions = []

        while self.recording:
            pass
        self.recText = False
        self.writeBuffer = None


    # old function used for executing old files
    def execMovements(self):
        for location, character, self.writeBufferLocal in self.instructions:
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
            if (character == 's'):  # used for adding buffer time
                pyautogui.moveTo(location, duration=2.0)
            if (character == 'w'):
                pyautogui.moveTo(location, duration=0.25)
                pyautogui.write(self.writeBufferLocal, interval=0.05)
            if (character == 'a'):
                pyautogui.moveTo(location, duration=0.25)
                pyautogui.hotkey('ctrl', 'a')
            if (character == 'o'):
                pyautogui.moveTo(location, duration=0.25)
                pyautogui.hotkey('ctrl', 'c')
            if (character == 'p'):
                pyautogui.moveTo(location, duration=0.25)
                pyautogui.hotkey('ctrl', 'v')
            if (character == 'enter'):
                pyautogui.moveTo(location, duration=0.25)
                pyautogui.press('enter')
            if (character == 'end'):
                break

    def Start(self):

        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()

        self.instructions = []

        print("NOTE: input is responsive until esc is pressed")

        action = None

        while (action != 'e' or action != 'exit'):

            action = input(
                "Enter r to record an action sequence\nEnter q to run an action sequence\nEnter t to convert an old script to a new one\nEnter u to upgrade pip\nEnter e to exit:\n")

            self.instructions = None
            self.instructions = []

            if (action == 'e' or action == 'exit'):
                break;

            if (action == 'u'):
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

            if (action == 'q'):
                name = input("Enter the file name (exclude extension type)\n")
                rawName = name
                name = name + ".py"

                dest = os.path.join(self.FILE_FOLDER, name)

                reTry = True

                while reTry:
                    try:
                        # will create the directory if necessary
                        reader = Utilities.safe_open(dest, 'rb')

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

                        for root, dirs, files in os.walk(self.FILE_FOLDER):
                            for file in files:
                                if file.endswith(".py"):
                                    # print(file)
                                    fileArr.append(file)

                        closestMatches = difflib.get_close_matches(rawName, fileArr, cutoff=0.4, n=5)

                        if (len(closestMatches) > 0):
                            print("Similar file names were found:")
                            nameNum = 1
                            for match in closestMatches:
                                print(str(nameNum) + " - " + match)
                                nameNum += 1

                            runAgain = input("Would you like to try one of these files? (y/n):\n")
                            if (runAgain == "y" or runAgain == "yes"):
                                reTry = True
                                selected_num = int(input("Which file would you like to run? (enter the id):\n"))

                                # resetting the variables to account for the new name
                                name = closestMatches[selected_num - 1].rsplit('.', 1)[0]
                                rawName = name
                                name = name + ".py"

                                dest = os.path.join(self.FILE_FOLDER, name)

                            else:
                                reTry = False
                        else:
                            reTry = False

            if (action == 't'):
                name_orig = input("Enter the old file name (exclude extension type)\n")
                name = name_orig + ".aseq"

                dest = os.path.join(self.FILE_FOLDER, name)

                reTry = True

                while reTry:

                    try:
                        reader = Utilities.safe_open(dest, 'rb')
                        try:
                            self.instructions = pickle.load(reader)

                            name2 = name_orig + ".py"

                            dest2 = os.path.join(self.FILE_FOLDER, name2)

                            reader2 = Utilities.safe_open(dest2, 'w')
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
                                for location, character, self.writeBufferLocal in self.instructions:

                                    if (character == 'c'):
                                        reader2.write("pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[
                                            1]) + ", duration=0.25)\n")
                                        reader2.write(
                                            "pyautogui.click(" + "({0}, {1})".format(location[0], location[1]) + ")\n")
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
                                        reader2.write("pyautogui.write(\'" + self.writeBufferLocal + "\', interval=0.05)\n")
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

                                print(self.instructions)
                            finally:
                                reader2.close()


                        finally:
                            reader.close()
                            reTry = False

                    except FileNotFoundError:
                        print("ERROR: file {0} not found!".format(name))

                        fileArr = []

                        for root, dirs, files in os.walk(self.FILE_FOLDER):
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

                                dest = os.path.join(self.FILE_FOLDER, name)

                            else:
                                reTry = False
                        else:
                            reTry = False

            if (action == 'r'):
                name = input("Enter the file name (exclude extension type)\n")
                rawName = name
                name = name + ".py"

                print(
                    "c - click\nd - double click\nf - right click\n` - toggle writing\ns - add waiting time\nl - move mouse to location\na - ctrl + A hotkey\no - ctrl + C hotkey\np - ctrl + V hotkey\ni - drag mouse (left click) to location\nx - press twice, once for the top left of the\n\tobject and once for the bottom right of the object\n\tThe program will later find this object and click the center\nz - press twice, once for the top left of the\n\tobject and once for the bottom right of the object\n\tThe program will later find this object and double-click the center\nu - press twice, once for the top left of the\n\tobject (to drag to) and once for the bottom right of the object\n\t(to drag to)\n\tThe program will later find this object and drag to the centre\nenter - presses enter (NOTE: it only records enter after the first\n"
                    + "\t\taction has been recorded AND you are NOT in writing-mode)\ne - end recording")

                dest = os.path.join(self.FILE_FOLDER, name)

                self.pic_dest = os.path.join("images", rawName)
                self.pic_dest_write_safe = re.escape(
                    os.path.join("images")) + "\\\\" + rawName

                reader = Utilities.safe_open(dest, 'w')

                dummyreader = Utilities.safe_open(os.path.join(self.FILE_FOLDER, "images", "dummyfile-ignoreme"), 'w')
                dummyreader.close()

                try:
                    self.recordMovements()
                    # pickle.dump(self.instructions, reader)
                    # using python script to make human readible instead now
                    reader.write("import subprocess\n")
                    reader.write("import sys\n")
                    reader.write("import pyautogui\n")
                    reader.write("def install(package):\n")
                    reader.write("\tsubprocess.check_call([sys.executable, \"-m\", \"pip\", \"install\", package])\n")
                    reader.write("\n\n#Ensures pip is installed:\nsubprocess.check_call([sys.executable, \"-m\", "
                                "\"ensurepip\", \"--default-pip\"])\n")
                    reader.write("\n\ninstall('pyautogui')\n")
                    reader.write("install('opencv-python')\n\n")
                    for location, character, self.writeBufferLocal in self.instructions:

                        if (character == 'c'):
                            reader.write(
                                "pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) + ", duration=0.25)\n")
                            reader.write("pyautogui.click(" + "({0}, {1})".format(location[0], location[1]) + ")\n")
                        if (character == 'd'):
                            reader.write(
                                "pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) + ", duration=0.25)\n")
                            reader.write("pyautogui.doubleClick(" + "({0}, {1})".format(location[0],
                                                                                        location[1]) + ", duration=0.1)\n")
                        if (character == 'f'):
                            reader.write(
                                "pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) + ", duration=0.25)\n")
                            reader.write("pyautogui.rightClick(" + "({0}, {1})".format(location[0], location[1]) + ")\n")
                        if (character == 's'):  # used for adding buffer time
                            reader.write(
                                "pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) + ", duration=2.0)\n")
                        if (character == 'l'):  # used for moving the mouse
                            reader.write(
                                "pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) + ", duration=0.5)\n")
                        if (character == 'w'):
                            reader.write(
                                "pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) + ", duration=0.25)\n")
                            reader.write("pyautogui.write(\'" + self.writeBufferLocal + "\', interval=0.05)\n")
                        if (character == 'a'):
                            reader.write("pyautogui.hotkey('ctrl', 'a')\n")
                        if (character == 'o'):
                            reader.write("pyautogui.hotkey('ctrl', 'c')\n")
                        if (character == 'p'):
                            reader.write("pyautogui.hotkey('ctrl', 'v')\n")
                        if (character == 'i'):
                            reader.write(
                                "pyautogui.dragTo(" + "({0}, {1})".format(location[0], location[1]) + ", duration=0.25, button='left')\n")
                        if (character == 'x'):
                            reader.write("worked = False\n")
                            reader.write("confidence_amount = 1.0\n")
                            reader.write("while(worked != True):\n")
                            reader.write("\ttry:\n")
                            reader.write(
                                "\t\tx, y = pyautogui.locateCenterOnScreen('" + self.pic_dest_write_safe + self.writeBufferLocal + ".png" + "', confidence=confidence_amount)\n")
                            reader.write("\t\tpyautogui.moveTo( (x, y), duration=0.25)\n")
                            reader.write("\t\tpyautogui.click((x, y))\n")
                            reader.write("\t\tworked = True\n")
                            reader.write("\texcept TypeError:\n\t\tconfidence_amount-=0.1\n")
                        if (character == 'z'):
                            reader.write("worked = False\n")
                            reader.write("confidence_amount = 1.0\n")
                            reader.write("while(worked != True):\n")
                            reader.write("\ttry:\n")
                            reader.write(
                                "\t\tx, y = pyautogui.locateCenterOnScreen('" + self.pic_dest_write_safe + self.writeBufferLocal + ".png" + "', confidence=confidence_amount)\n")
                            reader.write("\t\tpyautogui.moveTo( (x, y), duration=0.25)\n")
                            reader.write("\t\tpyautogui.doubleClick((x, y))\n")
                            reader.write("\t\tworked = True\n")
                            reader.write("\texcept TypeError:\n\t\tconfidence_amount-=0.1\n")
                        if (character == 'u'):
                            reader.write("worked = False\n")
                            reader.write("confidence_amount = 1.0\n")
                            reader.write("while(worked != True):\n")
                            reader.write("\ttry:\n")
                            reader.write(
                                "\t\tx, y = pyautogui.locateCenterOnScreen('" + self.pic_dest_write_safe + self.writeBufferLocal + ".png" + "', confidence=confidence_amount)\n")
                            reader.write("\t\tpyautogui.dragTo( (x, y), duration=0.5)\n")
                            reader.write("\t\tworked = True\n")
                            reader.write("\texcept TypeError:\n\t\tconfidence_amount-=0.1\n")

                        if (character == 'enter'):
                            reader.write(
                                "pyautogui.moveTo(" + "({0}, {1})".format(location[0], location[1]) + ", duration=0.25)\n")
                            reader.write("pyautogui.press('enter')\n")
                        if (character == 'end'):
                            break

                    print(self.instructions)
                finally:
                    reader.close()

if __name__ == "__main__":
    Controller().Start()
