import pyautogui
import time


gaali = input("Gaali idhar do?: ")

print("Switch to your application in 10 seconds")

time.sleep(10)

for i in range(100):
    pyautogui.typewrite(gaali)
    pyautogui.press('enter')
    time.sleep(0.1)
