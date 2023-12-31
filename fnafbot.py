import pyautogui
import time
import FileHandler as fh

pyautogui.FAILSAFE = False

LONGER_DELAY = 0.32
LIGHT_DELAY = 0.4
DELAY = 0.17
filehandler = fh.FileHandler()

positions = {
    "new game" : (231, 422),
    "continue" : (226, 491),
    "look left" : (63, 406),
    "look right" : (1201, 454),
    "right light" : (1216, 465),
    "right door" : (1218, 348),
    "left light" : (58, 456),
    "left door" : (52, 347),
    "camera" : (567, 709),
    "neutral" : (628, 377),
    "1a" : (984, 350),
    "1b" : (959, 412),
    "1c" : (929, 485),
    "2a" : (979, 597),
    "2b" : (981,641),
    "3" : (901, 585),
    "4a" : (1084, 602),
    "4b" : (1089, 647),
    "5" : (858, 442),
    "6" : (1181, 570),
    "7" : (1199, 434)
}



def start():
    global positions
    positions = filehandler.read()

def start_game():
    pyautogui.moveTo(292, 637)
    pyautogui.click()

def getMousePosition():
    pos = pyautogui.position()
    return pos

def click(pos):
    pyautogui.click(pos[0], pos[1])

def move(pos):
    pyautogui.moveTo(pos[0], pos[1])

def moveDelay(pos):
    pyautogui.moveTo(pos[0], pos[1], DELAY)

def start():
    pos = positions["new game"]
    click(pos)

def toggleCam():
    move(positions["neutral"])
    moveDelay(positions["camera"])
    moveDelay(positions["neutral"])


def continue_game():
    pos = positions["continue"]
    click(pos)

def look_left():
    pos = positions["look left"]
    move(pos)

def look_right():
    pos = positions["look right"]
    move(pos)

def left_door():
    move(positions["left door"])
    time.sleep(LONGER_DELAY)
    click(positions["left door"])

def right_door():
    move(positions["right door"])
    time.sleep(LONGER_DELAY)
    click(positions["right door"])

def left_light():
    move(positions["left light"])
    time.sleep(LONGER_DELAY)
    click(positions["left light"])

def right_light():
    move(positions["right light"])
    time.sleep(LONGER_DELAY)
    click(positions["right light"])

def press(loc):
    click(positions[loc])

def bind(command):
    if command in positions:
        positions[command] = pyautogui.position()
    filehandler.write()