import config
import pyautogui
import time


    


config.initialize()
config.countdown()

with open("messages.txt",'r') as messages:
    for line in messages:
        pyautogui.typewrite(line,interval=.01)
        time.sleep(config.interval)

