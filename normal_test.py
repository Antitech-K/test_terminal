import time
import os
from locators.forms_pages_locators import FormsPagesLocators
from scenarios.scenariо_LD import Tonometr
from scenarios.scenariо_berrcom import Termometr
from scenarios.scenario_ALCO import Alco
#from pages.start_page import LoadStartPage



def shutdown_rodos():
    for x in range(16):
        a = "/opt/RODOS4/RODOS4 --id 4798 --c" +str(x) + " 0"
        os.system(a)
    return "Усё" 

os.system("/opt/RODOS4/RODOS4 --id 4798 --c8 128") # включение чайника
os.system("/opt/RODOS4/RODOS4 --id 4798 --c4 128") # включение компрессор

time.sleep(4)
FormsPagesLocators.Authorization(1) 
FormsPagesLocators.PREVIEW_PAGE() #подтверждение страницы превью
Tonometr.runLD()
time.sleep(20)
Termometr.runBERRCOM()


#алкотестирование
Alco.runDingoE200()

os.system("/opt/RODOS4/RODOS4 --id 4798 --c8 0")
os.system("/opt/RODOS4/RODOS4 --id 4798 --c4 0")
  
time.sleep(1)
shutdown_rodos()   