import PIL
from pynput.keyboard import Key, Controller

keyboard = Controller()


x = 1920 / 2 - 500
y = 1080 / 2

def get_pixel_colour(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[i_x, i_y]

def press_space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    
oldpxl = get_pixel_colour(x, y)
while(True):
      currentpxl = get_pixel_colour(x, y)
      if(oldpxl != currentpxl):
          print("Yamete")
          oldpxl = currentpxl
          press_space()
        
