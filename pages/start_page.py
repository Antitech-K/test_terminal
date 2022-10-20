import pyautogui
import time
import os


class Load_start:
    os.system("DISPLAY=:0 NODE_ENV=production aurora")
    time.sleep(2)
    while pyautogui.locateCenterOnScreen('start_load.png', confidence=0.99) ==None:
        time.sleep(1)
    pyautogui.press('f11') #Нажимаем клавишу F11
    time.sleep(0.5)