# tesseract init
try:
    from PIL import Image, ImageGrab
except ImportError:
    import Image, ImageGrab
import pytesseract
import numpy as nm
import cv2
import solve
import pyperclip
import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

# bbox
left = 658
upper = 802
right = 1230
lower = 909

# enter
enter_box = 654, 969

delay = 0.1

pytesseract.pytesseract.tesseract_cmd = r'D:\Games\tessera\tesseract.exe'

#pynput shit
mouse = MouseController()
keyboard = KeyboardController()

def detect_prompt(tesstr):
    return tesstr.split(":")[1]


def enter_solution(solution):
    pyperclip.copy(solution)
    mouse.position = (enter_box)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl.value)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl.value)
    keyboard.press(Key.enter.value)
    keyboard.release(Key.enter.value)

def main():
    while True:
        image = ImageGrab.grab(bbox = (left, upper, right, lower))
        tesstr = pytesseract.image_to_string( 
                    cv2.cvtColor(nm.array(image), cv2.COLOR_BGR2GRAY),  
                    lang ='eng') 
        if "Quick!" in tesstr:
            print(tesstr)
            prompt = "".join(char for char in detect_prompt(tesstr).lower() if char.isalpha())
            print(prompt)
            solution = solve.solve(prompt)
            time.sleep(delay)
            enter_solution(solution)


main()