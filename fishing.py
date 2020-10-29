import pyautogui
import time, keyboard


'''
This script assumes you have a 1920x1080 monitor, and are running minecraft in windowed.
A full screenshot is attached of my view when playing it.
Adjust region to suit your needs if playing in lower resolutions.
'''
# Creates a box, starting at (935, 655) 
# with a width and height of (50, 60)
REGION = (935,655,50,60)
# Key to toggle with
TOGGLE_KEY = 'num 0'

class FishBot():
    def __init__(self):
        self.toggled = False
    
    def toggle(self):
        self.toggled = not self.toggled

    def auto_fish(self):

        #find center of hook on screen
        self.hook = pyautogui.locateCenterOnScreen('images/hook.png', region=REGION, confidence=.45)

        # if the hook is present do nothing
        if self.hook is not None:
            pass
        # if theres no hook, either we have a fish on line
        # or we've just reeled in, so right click
        elif self.hook is None:
            pyautogui.rightClick()
            time.sleep(1)
        else:
            print('Error')

bot = FishBot()

while True:
    if keyboard.is_pressed(TOGGLE_KEY):
        bot.toggle()
        if bot.toggled:
            print('Active')
        else:
            print('Deactived')
        while keyboard.is_pressed(TOGGLE_KEY):
            pass
        
    if bot.toggled:
        bot.auto_fish()
