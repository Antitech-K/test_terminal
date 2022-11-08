import os, sys
import time
import pyautogui

class ERRORdevice:
    def ERROR():
        path_error = os.path.join('locators', 'Error_measure.png')
        if pyautogui.locateCenterOnScreen(path_error) != None:
            return print("Эррор, блять"), shutdown_rodos(), sys.exit()
            sys.exit(0)
        pass    