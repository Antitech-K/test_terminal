import pyautogui
import time
import os, sys

time.sleep(1)
class LoadStartPage:
    os.system("DISPLAY=:0 NODE_ENV=production aurora")
    time.sleep(3)
    counter = 0
    
    path_start =  os.path.join('pages', 'start_load.png')
    #pyautogui.press('f11') #полноэкранный режим
    time.sleep(1)
    if pyautogui.locateCenterOnScreen(path_start, confidence=0.9) ==None:
        counter += 1
        if counter == 10:
            print("Хюстон, у нас проблемы на старте")
            sys.exit(0) # - 0 код выхода при не обнаружении скрина
    