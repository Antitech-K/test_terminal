import time
import os
from locators.forms_pages_locators import FormsPagesLocators
from scenarios.scenariо_LD import Tonometr
from scenarios.scenariо_berrcom import Termometr
from scenarios.scenario_ALCO import Alco
from scenarios.scenarioERRORdevice import ERRORdevice
#from pages.start_page import LoadStartPage


def shutdown_rodos():
    for x in range(16):
        a = "/opt/RODOS4/RODOS4 --id 4798 --c" +str(x) + " 0"
        os.system(a)
        time.sleep(0.1)
    return "Усё" 

os.system("/opt/RODOS4/RODOS4 --id 4798 --c8 128") # включение чайника
os.system("/opt/RODOS4/RODOS4 --id 4798 --c4 128") # включение компрессор
'''
os.system("/opt/RODOS4/RODOS4 --id 4798 --c9 128")
time.sleep(0.8)
os.system("/opt/RODOS4/RODOS4 --id 4798 --c9 0")
'''
time.sleep(3)
FormsPagesLocators.Authorization(1) 
FormsPagesLocators.PREVIEW_PAGE() #подтверждение страницы превью
Tonometr.runLD()
ERRORdevice.ERROR()
time.sleep(30)
ERRORdevice.ERROR()
Termometr.runBERRCOM()
ERRORdevice.ERROR()
Alco.runDingoE200() #алкотестирование

#Выключение
os.system("/opt/RODOS4/RODOS4 --id 4798 --c8 0")
os.system("/opt/RODOS4/RODOS4 --id 4798 --c4 0")
  
time.sleep(1)
shutdown_rodos()   