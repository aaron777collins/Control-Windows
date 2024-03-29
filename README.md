# Control Windows By Recording Actions
This is a simple program to automate tasks on your pc.
First, you record a "sequence" of actions for the program to repeat.
Then, analyze the recorded actions and make sure it fits your needs.
Finally, run the script and watch your computer automate those annoying,
repetitive tasks.

Recording Keys:

    c - click

    d - double-click

    f - right-click

    s - wait for 2 seconds

    l - move mouse to location

    ` - toggle writing mode

    a - ctrl + A hotkey

    o - ctrl + C hotkey

    p - ctrl + V hotkey

    x - press twice, once for the top left of the object and once for the bottom right of the object. The program will try to
    find this object later and click the center.

    z - press twice, once for the top left of the object and once for the bottom right of the object. The program will try to
    find this object later and double-click the center.

    u - press twice, once for the top left of the object (to drag to) and once for the bottom right of the object. The program will try to
    find this object to drag to later (drags to centre).

    enter - presses enter (NOTE: it only records enter after the first 
            action has been recorded AND you are NOT in writing-mode)

    e - end sequence



NOTE:

As a fail-safe, you can move your mouse to the top left of your screen to crash the program.
This will prevent your computer from going wild while running an action.

This program was written with globals and may have a bug or two but it is
pretty useful. Feel free to fix any bugs or rewrite the code in a better
way! I only wrote this because I'm pretty lazy when it comes to repetitive tasks (and to learn python)

Before installing, make sure you install python (v3) and put the directory of
your python install within the PATH environment variable. (Check the box on install)

To make running this program easier, create a batch file(.bat) with the following code:

    @echo off
    python "controlWindows.py"
    
I find it is easiest to paste this into notepad, click File > Save As
and then name it "runWC.bat". Don't forget to select the file type "All Files (\*.*)"

Then, place the new batch file in the same directory as this project. All files will
generate within the project folder (images are in "[project folder]\images")

*THIS IS IMPORTANT! Do not label your script as controlWindows or checkDependencies. You will overwrite a source file.*

(Code was based off of this tutorial:

https://automatetheboringstuff.com/2e/chapter20/

and then implemented to my needs)

Enjoy!
