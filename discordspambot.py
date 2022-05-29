import pyautogui
import time

time.sleep(3)
f = open("rank", "r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(3)
