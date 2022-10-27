import pyautogui
import time
import os


class FormsPagesLocators:

    def AUTHORIZATION():
        START_AUTHORIZATION = pyautogui.leftClick(1030, 185, duration=1)
        pass

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
        path_verification = os.path.join('locators', 'verification.png')
        while pyautogui.locateCenterOnScreen(path_verification, confidence=0.95) == None:
            time.sleep(1)
            temp += 1
            if temp == 3:
                return print("Хюстон, у нас проблемы на экране подтверждения")
        pyautogui.leftClick(1030, 690, duration=0.25)

        path_inspection_type =  os.path.join('locators', 'pre-trip_type.png')
        while pyautogui.locateCenterOnScreen(path_inspection_type) == None:
            time.sleep(1)
            temp += 1
            if temp == 3:
                return print("Хюстон, у нас проблемы на экране типа осмотра")
        x, y =pyautogui.locateCenterOnScreen(path_inspection_type)
        pyautogui.leftClick(x, y, duration=0.25)
        pass

    def PREVIEW_PAGE():
        temp = 0
        path_preview =  os.path.join('scenarios', 'preview.png')
        while pyautogui.locateCenterOnScreen(path_preview, confidence=0.98) == None:
            time.sleep(0.5)
            temp += 1
            if temp == 6:
                return print("Хюстон, у нас проблемы на экране preview")
        pyautogui.leftClick(1030, 690, duration=0.25)
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
    

