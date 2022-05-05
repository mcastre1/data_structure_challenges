import pyautogui

while True:
    coords = pyautogui.locateCenterOnScreen('./melee.png', grayscale = True, confidence=.8)
    if coords != None:
        #print("coords not none")
        pyautogui.rightClick(coords.x, coords.y)