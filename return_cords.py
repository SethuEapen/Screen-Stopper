import PIL
from pynput.keyboard import Key, Controller
import keyboard
import time
import pyautogui

while(True):
    if(keyboard.is_pressed('o')):
        print(pyautogui.position())
