import os, sys
import time
import pyautogui

class Tonometr:
    def runLD():
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c10 128")
        temp = 0
        path_tonometr =  os.path.join('scenarios', 'start_tonometr.png')
        while pyautogui.locateCenterOnScreen(path_tonometr, confidence=0.98) == None:
            time.sleep(0.5)
            temp += 1
            if temp == 6:
                return print("Хюстон, у нас проблемы на старте тонометра")
                sys.exit(0)
        pyautogui.leftClick(1040, 690, duration=0.25)