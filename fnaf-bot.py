import pyautogui
import time

new_game  = (292, 637)

pyautogui.FAILSAFE = False

def start_game():
    pyautogui.moveTo(292, 637)
    pyautogui.click()