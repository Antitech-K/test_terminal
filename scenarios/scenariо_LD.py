import os
from time import time
import pyautogui

class Tonometr:
    def RUN_LD():
        temp = 0
        while pyautogui.locateCenterOnScreen('preview.png', confidence=0.98) == None:
            time.sleep(0.5)
            temp += 1
            if temp == 6:
                return print("Хюстон, у нас проблемы на экране preview")

        os.system("/opt/RODOS4/RODOS4 --id 4798 --c10 128")
        pyautogui.leftClick(1030, 690, duration=0.25)
        temp = 0
        while pyautogui.locateCenterOnScreen('start_tonometr.png', confidence=0.98) == None:
            time.sleep(0.5)
            temp += 1
            if temp == 6:
                return print("Хюстон, у нас проблемы на старте тонометра")