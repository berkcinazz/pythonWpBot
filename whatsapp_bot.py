import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responses import response

# Requires opencv-python package for image recognition confidence
mouse = Controller()


# Instructions for our WhatsApp Bot
class WhatsApp:

    # Defines the starting values
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    def alt_tab(self):
        pt.hotkey('alt', 'tab', duration=self.speed)

    # Navigate to the green dots for new messages
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_circle_paperclip.png', confidence=.8)
            pt.moveTo(position[0], position[1], duration=0.5)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick()
        except Exception as e:
            print('Exception (nav_green_dot): ', e)

    # Navigates to the message we want to respond to
    def nav_message(self):
        try:
            playbutton = pt.locateOnScreen('play_button.png')
            position = pt.locateOnScreen('smileys_paperclip.png', confidence=.6)
            x = position[0]
            y = position[1]
            pt.moveTo(position[0], position[1], duration=self.speed)
            pt.moveRel(90, -40, duration=self.speed)  # x,y has to be adjusted depending on your computer
            if pt.pixelMatchesColor(int(x + 110), int(y - 55), (255, 255, 255), tolerance=10):
                print("is white")
            else:
                print("is not white")
            if playbutton is None:
                print("Move on")
            else:
                print('Just message!')
        except Exception as e:
            print('Exception (nav_message): ', e)

    # Copies the message that we want to process
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(50, -130, duration=self.speed)  # x,y has to be adjusted depending on your computer
        mouse.click(Button.left, 1)
        sleep(1)

        # Gets and processes the message
        self.message = pc.paste()
        print('User says: ', self.message)

    # Navigate to our message input box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('smileys_paperclip.png', confidence=.6)
            pt.moveTo(position[0], position[1], duration=self.speed)
            pt.moveRel(200, 15, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ', e)

    # Sends the message to the user
    def send_message(self):
        try:
            var = "send_message worked"
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('You say: ', bot_response)
                pt.typewrite(var, interval=.1)
                pt.typewrite('\n')  # Sends the message (Disable it while testing)

                # Assigns them the same message
                self.last_message = self.message
            else:
                print('No new messages...')

        except Exception as e:
            print('Exception (send_message): ', e)

    # Close response box
    def nav_x(self):
        try:
            position = pt.locateOnScreen('x.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10, 10, duration=self.speed)  # x,y has to be adjusted depending on your computer
            mouse.click(Button.left, 1)
        except Exception as e:
            print('Exception (nav_x): ', e)


# Initialises the WhatsApp Bot
wa_bot = WhatsApp(speed=.60, click_speed=.60)

# Run the programme in a loopCool!
while True:
    wa_bot.alt_tab()
    wa_bot.nav_green_dot()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()

    # Delay between checking for new messages
    sleep(5)
