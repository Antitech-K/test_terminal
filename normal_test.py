import time
import os
from locators.forms_pages_locators import FormsPagesLocators
from scenarios.scenariо_LD import Tonometr
from scenarios.scenariо_berrcom import Termometr
from pages.start_page import load_start


os.system("/opt/RODOS4/RODOS4 --id 4798 --c8 128")
os.system("/opt/RODOS4/RODOS4 --id 4798 --c4 128")

FormsPagesLocators.START_AUTHORIZATION(0)
Tonometr.RUN_LD()
time.sleep(20)
Termometr.RUN_BERRCOM()

#алкотестирование
time.sleep(10)
os.system("/opt/RODOS4/RODOS4 --id 4798 --c0 128")
time.sleep(2)
os.system("/opt/RODOS4/RODOS4 --id 4798 --c0 0")
time.sleep(20)
os.system("/opt/RODOS4/RODOS4 --id 4798 --c0 128")
time.sleep(12)
os.system("/opt/RODOS4/RODOS4 --id 4798 --c0 0")
time.sleep(5)

os.system("/opt/RODOS4/RODOS4 --id 4798 --c8 0")
os.system("/opt/RODOS4/RODOS4 --id 4798 --c4 0")

def shutdown_rodos():
    for x in range(16):
        a = "/opt/RODOS4/RODOS4 --id 4798 --c" +str(x) + " 0"
        os.system(a)
    return "Усё"   