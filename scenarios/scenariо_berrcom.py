import os
import time
import pyautogui

class Termometr:
    def runBERRCOM():
        temp = 0
        path_termometr =  os.path.join('scenarios', 'berrcom.png')
        while pyautogui.locateCenterOnScreen(path_termometr, confidence=0.90) == None:
            time.sleep(2)
            temp += 1
            if temp == 20:
                return print("Хюстон, у нас проблемы на экране термометрии")
        time.sleep(1)
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c9 128")
        time.sleep(0.5)
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c9 0")