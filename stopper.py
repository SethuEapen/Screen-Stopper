import PIL
from pynput.keyboard import Key, Controller
import keyboard
import time

keyboardz = Controller()


x = 640
y = 800

def get_pixel_colour(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[i_x, i_y]

def press_space():
    keyboardz.press(Key.space)
    keyboardz.release(Key.space)

    
oldpxl = get_pixel_colour(x, y)
while(True):
        if(not keyboard.is_pressed('o')):
              currentpxl = get_pixel_colour(x, y)
              if(oldpxl != currentpxl):
                  print("Yamete")
                  oldpxl = currentpxl
                  press_space()
                  time.sleep(.1)
        
