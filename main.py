import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(1)

position1 = pt.locateOnScreen("smileys_paperclip.png",confidence=.4)
x = position1[0]
y = position1[1]


def get_message():
    global x,y
    position = pt.locateOnScreen("smileys_paperclip.png",confidence=.4)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x + 95 , y - 43, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(20,-130)
    pt.click()
    receivedMsg = pyperclip.paste()
    return receivedMsg


def post_response(message):
    global x,y
    position = pt.locateOnScreen("smileys_paperclip.png",confidence=.4)
    x=position[0]
    y=position[1]
    pt.moveTo(x+200, y+20,duration=.5)
    pt.click()
    pt.typewrite(message,interval =.01)
    #pt.typewrite("\n", interval=.01)


def process_response(message):
    random_num = random.randrange(3)
    if "?" in str(message).lower():
        return "Don't ask me questions."
    if random_num == 0:
        return "0"
    elif random_num == 1:
        return "1" 
    else:
        return "2"

def check_for_new_messages():
    pt.moveTo(x+100, y-30,duration=.5)
    while True:
        try:
            position = pt.locateOnScreen("green_circle_paperclip.png",confidence=.8)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new message")
        if pt.pixelMatchesColor(int(x + 50), int(y - 35), (255,255,255), tolerance=10):
            print("is white")
            proccessed_response = process_response(get_message())
            post_response(proccessed_response)
        else:
            print("no messages")
        sleep(5)





check_for_new_messages()
