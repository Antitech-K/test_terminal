import pyautogui
import time
import os

time.sleep(5)
class LoadStartPage:
    os.system("DISPLAY=:0 NODE_ENV=production aurora")
    time.sleep(3)
    counter = 0
    
    path_start =  os.path.join('pages', 'start_load.png')
    while pyautogui.locateCenterOnScreen(path_start, confidence=0.6) ==None:
        time.sleep(1)
        counter += 1
        if counter == 10:
            print("Хюстон, у нас проблемы на старте")

    pyautogui.press('f11') #полноэкранный режим
    time.sleep(0.5)