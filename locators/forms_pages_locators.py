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
        temp = 0
        while pyautogui.locateCenterOnScreen('verification.png', confidence=0.95) == None:
            time.sleep(1)
            temp += 1
            if temp == 3:
                return print("Хюстон, у нас проблемы на экране подтверждения")
        pyautogui.leftClick(1030, 690, duration=0.25)

        while pyautogui.locateCenterOnScreen('inspection_type.png') == None:
            time.sleep(1)
            temp += 1
            if temp == 3:
                return print("Хюстон, у нас проблемы на экране типа осмотра")
        x, y =pyautogui.locateCenterOnScreen('inspection_type.png')
        pyautogui.leftClick(x, y, duration=0.25)
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
    

