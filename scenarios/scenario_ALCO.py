import os, sys
import time
import pyautogui

class Alco:
    def runDingoE200():
        time.sleep(1)
        path_alco = os.path.join('scenarios', 'alco_start.png')
        if pyautogui.locateCenterOnScreen(path_alco) == None:
            return print("Хюстон, у нас проблемы на старте алкотестера")
            sys.exit(0)
        time.sleep(10)
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c0 128")
        time.sleep(2)
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c0 0")
        pass