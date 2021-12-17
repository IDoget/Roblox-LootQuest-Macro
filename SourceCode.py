# Developed by IDoget and Dogwarrior24 #
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

area = input('Enter 1 for Ice Warrior \nEnter 2 for Arch Demon \nEnter 3 for Quatermaster \nEnter 4 for Pharaohs Guard\nEnter X to Close\n : ')
kills = 0
speedboost = False


if area == 'x' or area == 'X':
    exit()
elif area == '1':
    print('Ice Warrior selected\n\n\n\n\n')
    speed = input('Do you have speed gamepass (Y/N)\n : ')

    if speed == 'Y' or speed == 'y':
        speedboost = True
    elif speed == 'N' or speed == 'n':
        speedboost = False
    else:
        exit('Invalid Input')
    
    print('You will be given 10 seconds to tab into roblox and position your roblox character as seen on github.')
    time.sleep(3)
    print('To stop the macro hold Q')
    time.sleep(3)
    _ = input('Press Enter to begin macro!\n')

    for countdown in range(10, 0, -1):
        if countdown == 5 or countdown == 10:
            print(str(countdown) + '        REMINDER TO ENABLE SHIFT LOCK')
        else:
            print(countdown)
        time.sleep(1)

    if speedboost == False:
        while not keyboardOutput.is_pressed('q'):
            time.sleep(8 + (0.97 * (2/3)))
            mouseInput.press(Button.left)
            time.sleep(0.2)
            mouseInput.release(Button.left)
            time.sleep(0.4)
            keyboardInput.press('a')
            time.sleep(0.97 * (2/3))
            keyboardInput.release('a')
            time.sleep(0.2)
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.4)
            keyboardInput.press('d')
            time.sleep(0.97 * (2/3))
            keyboardInput.release('d')
            kills += 2
        print(f'Total kills: {kills}')
    else:
        while not keyboardOutput.is_pressed('q'):
            time.sleep(8)
            mouseInput.press(Button.left)
            time.sleep(0.2)
            mouseInput.release(Button.left)
            time.sleep(0.4)
            keyboardInput.press('a')
            time.sleep(0.97)
            keyboardInput.release('a')
            time.sleep(0.2)
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.4)
            keyboardInput.press('d')
            time.sleep(0.97)
            keyboardInput.release('d')
            kills += 2
        print(f'Total kills: {kills}')
elif area == '2':
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
    print('To stop the macro hold Q')
    time.sleep(3)
    _ = input('Press Enter to begin macro!\n')

    for countdown in range(10, 0, -1):
        if countdown == 5 or countdown == 10:
            print(str(countdown) + '        REMINDER TO ENABLE SHIFT LOCK')
        else:
            print(countdown)
        time.sleep(1)

    if speedboost == False:
        while not keyboardOutput.is_pressed('q'):
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
            kills += 2
        print(f'Total kills: {kills}')
    else:
        while not keyboardOutput.is_pressed('q'):
            time.sleep(6 + (1.845 * (2/3)))
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.845 * (2/3))
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.845 * (2/3))
            keyboardInput.release('d')
            kills += 2
        print(f'Total kills: {kills}')
elif area == '3':
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
    print('To stop the macro hold Q')
    time.sleep(3)
    _ = input('Press Enter to begin macro!\n')
    
    for countdown in range(10, 1, -1):
        if countdown == 5 or countdown == 10:
            print(str(countdown) + '        REMINDER TO ENABLE SHIFT LOCK')
        else:
            print(countdown)
        time.sleep(1)
    
    if speedboost == False:
        while not keyboardOutput.is_pressed('q'):
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
            kills += 2
        print(f'Total kills: {kills}')
    else:
        while not keyboardOutput.is_pressed('q'):
            time.sleep(6 + (1.845 * (2/3)))
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.845 * (2/3))
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.845 * (2/3))
            keyboardInput.release('d')
            kills += 2
        print(f'Total kills: {kills}')
elif area == '4':
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
    print('To stop the macro hold Q')
    time.sleep(3)
    _ = input('Press Enter to begin macro!\n')
    
    for countdown in range(10, 1, -1):
        if countdown == 5 or countdown == 10:
            print(str(countdown) + '        REMINDER TO ENABLE SHIFT LOCK')
        else:
            print(countdown)
        time.sleep(1)

    if speedboost == False:
        while not keyboardOutput.is_pressed('q'):
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
            kills += 2
        print(f'Total kills: {kills}')
    else:
        while not keyboardOutput.is_pressed('q'):
            time.sleep(6 + (1.75 * (2/3)))
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.36)
            keyboardInput.press('a')
            time.sleep(1.75 * (2/3))
            keyboardInput.release('a')
            mouseInput.press(Button.left)
            time.sleep(0.1)
            mouseInput.release(Button.left)
            time.sleep(0.465)
            keyboardInput.press('d')
            time.sleep(1.75 * (2/3))
            keyboardInput.release('d')
            kills += 2
        print(f'Total kills: {kills}')
else:
    exit('Invalid Input')
