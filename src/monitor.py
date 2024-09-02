import pyautogui
import sys
import time

try:
    while True:
        x, y = pyautogui.position()
        sys.stdout.write(f'\r{x}, {y}        ')
        sys.stdout.flush()
    	#time.sleep(1)
except KeyboardInterrupt:
    print('\nExit.')