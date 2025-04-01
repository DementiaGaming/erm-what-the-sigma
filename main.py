import pyautogui
import random
import playsound
import keyboard

running = True
keys = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
          "a", "s", "d", "f", "g", "h", "j", "k", "l",
          "z", "x", "c", "v", "b", "n", "m"]

sounds = ["jonkler.mp3"]

while running:
    for i in range(len(keys)):
        tempKey = keys[i]
        if keyboard.is_pressed(tempKey):
            print("t")
            if random.randint(1, 10000) == 1:
                tempSound = random.choice(sounds)
                playsound.playsound(f"sounds/{tempSound}.mp3", False)
    
    