import os
import time
import pyautogui

class Alco:
    def runDingoE200():
        time.sleep(10)
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c0 128")
        time.sleep(2)
        os.system("/opt/RODOS4/RODOS4 --id 4798 --c0 0")
        pass