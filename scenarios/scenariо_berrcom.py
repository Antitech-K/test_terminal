import os
from time import time
import pyautogui

class Termometr:
    def RUN_BERRCOM():
        temp = 0
        while pyautogui.locateCenterOnScreen('berrcom.png', confidence=0.90) == None:
            time.sleep(2)
            temp += 1
            if temp == 20:
                return print("Хюстон, у нас проблемы на экране термометрия")
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c9 128")
        time.sleep(0.5)
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c9 0")