import pyautogui
import time
import os


class Load_start:
    os.system("DISPLAY=:0 NODE_ENV=production aurora")
    time.sleep(2)
    counter = 0
    while pyautogui.locateCenterOnScreen('start_load.png', confidence=0.99) ==None:
        time.sleep(1)
        counter += 1
        if counter == 10:
            print("Хюстон, у нас проблемы на экране термометрия")

    pyautogui.press('f11') #Нажимаем клавишу F11
    time.sleep(0.5)