# Developed by IDoget. #
# Do not edit, replicate, or sell without my permission!!! #
# If you have any bug reports please DM me on discord; IDoget#6840 #

import time
import keyboard as keyboardOutput
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController

keyboardInput = keyboardController()
mouseInput = mouseController()

area = input('Enter 1 for Arch Demon \nEnter 2 for Quatermaster \nEnter 3 for Pharaohs Guard \n[COMING SOON] Bandit general \nEnter X to Close\n : ')
speedboost = False


if area == 'x' or area == 'X':
    exit()
elif area == '1':
    print('Arch Demon selected\n\n\n\n\n')
    speed = input('Do you have speed gamepass (Y/N)\n : ')

    if speed == 'Y' or speed == 'y':
        speedboost = True
    elif speed == 'N' or speed == 'n':
        speedboost = False
    else:
        exit('Invalid Input')
    
    print('You will be given 10 seconds to tab into roblox and position your roblox character as seen on github.')
    time.sleep(3)
    print('To stop the macro press ctrl + c WITH THIS WINDOW OPEN')
    time.sleep(3)
    _ = input('Press Enter to begin macro!\n')

    for countdown in range(10, 0, -1):
        if countdown == 5 or countdown == 10:
            print(str(countdown) + '        REMINDER TO ENABLE SHIFT LOCK')
        else:
            print(countdown)
        time.sleep(1)

    if speedboost == False:
        while True:
            if keyboardOutput.is_pressed('x'):
                break
            time.sleep(6)
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.845)
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.845)
            keyboardInput.release('d')
    else:
        while True:
            if keyboardOutput.is_pressed('x'):
                break
            time.sleep(6)
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.845 + (1.845/2))
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.845 + (1.845/2))
            keyboardInput.release('d')
    exit()
elif area == '2':
    print('Quatermaster selected\n\n\n\n\n')
    speed = input('Do you have speed gamepass (Y/N)\n : ')

    if speed == 'Y' or speed == 'y':
        speedboost = True
    elif speed == 'N' or speed == 'n':
        speedboost = False
    else:
        exit('Invalid Input')

    print('You will be given 10 seconds to tab into roblox and position your roblox character as seen on github.')
    time.sleep(3)
    print('To stop the macro press ctrl + c WITH THIS WINDOW OPEN')
    time.sleep(3)
    _ = input('Press Enter to begin macro!\n')
    
    for countdown in range(10, 1, -1):
        if countdown == 5 or countdown == 10:
            print(str(countdown) + '        REMINDER TO ENABLE SHIFT LOCK')
        else:
            print(countdown)
        time.sleep(1)
    
    if speedboost == False:
        while True:
            if keyboardOutput.is_pressed('x'):
                break
            time.sleep(6)
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.845)
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.845)
            keyboardInput.release('d')
    else:
        while True:
            if keyboardOutput.is_pressed('x'):
                break
            time.sleep(6)
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.845 + (1.845/2))
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.845 + (1.845/2))
            keyboardInput.release('d')
    exit()
elif area == '3':
    print('Pharaohs Guard selected\n\n\n\n\n')
    speed = input('Do you have speed gamepass (Y/N)\n : ')

    if speed == 'Y' or speed == 'y':
        speedboost = True
    elif speed == 'N' or speed == 'n':
        speedboost = False
    else:
        exit('Invalid Input')
    
    print('You will be given 10 seconds to tab into roblox and position your roblox character as seen on github.')
    time.sleep(3)
    print('To stop the macro press ctrl + c WITH THIS WINDOW OPEN')
    time.sleep(3)
    _ = input('Press Enter to begin macro!\n')
    
    for countdown in range(10, 1, -1):
        if countdown == 5 or countdown == 10:
            print(str(countdown) + '        REMINDER TO ENABLE SHIFT LOCK')
        else:
            print(countdown)
        time.sleep(1)

    if speedboost == False:
        while True:
            if keyboardOutput.is_pressed('x'):
                break
            time.sleep(6)
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.75)
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.75)
            keyboardInput.release('d')
    else:
        while True:
            if keyboardOutput.is_pressed('x'):
                break
            time.sleep(6)
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.75 + (1.75/2))
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.75 + (1.75/2))
            keyboardInput.release('d')
    exit()
else:
    exit('Invalid Input')
