import pyautogui
import time


class FormsPagesLocators:

    def AUTHORIZATION():
        START_AUTHORIZATION = pyautogui.leftClick(1030, 185, duration=1)

    def PRINT_STICKER():
        pyautogui.leftClick(1030, 305, duration=0.25)
        pyautogui.leftClick(1030, 185, duration=0.25)
        pass
    def START_AUTHORIZATION(num_user):
        START_AUTHORIZATION = pyautogui.leftClick(1030, 185, duration=1)
        pyautogui.leftClick(1030, 210, duration=0.25)
        time.sleep(0.25)
        pyautogui.write('000'+ str(num_user))
        pyautogui.leftClick(1030, 690, duration=0.25)
        time.sleep(0.25)
        pyautogui.leftClick(1030, 690, duration=0.25)
        pyautogui.leftClick(1030, 185, duration=0.25)

        pass
    def NEXT_PAGE():
        pyautogui.leftClick(1030, 690, duration=0.25)
        pass
    def ACQUAINTANCE_PAC():
        ACQUAINTANCE_PAC = pyautogui.leftClick(1030, 430, duration=1)
        pass
    def HELPING():
        HELPING = pyautogui.leftClick(1225, 45)
        pass
    

