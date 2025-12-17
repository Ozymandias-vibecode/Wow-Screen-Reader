import keyboard
import pyautogui
import time

def macro_action():
    time.sleep(0.1)  # small delay so key release finishes
    pyautogui.write("R1", interval=0.02)  # example text
    pyautogui.press("enter")

keyboard.add_hotkey('ctrl+alt+f9', macro_action)

print("Macro running... Press ESC to quit.")
keyboard.wait('esc')