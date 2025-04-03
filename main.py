import pyautogui
import random
import playsound
import keyboard

running = True
keys = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
          "a", "s", "d", "f", "g", "h", "j", "k", "l",
          "z", "x", "c", "v", "b", "n", "m"]

while running:
    for i in range(len(keys)):
        tempKey = keys[i]
        if keyboard.is_pressed(tempKey):
            print("t")
            playsound.playsound(f"sounds/metalPipe.mp3", False)