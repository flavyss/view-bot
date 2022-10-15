import pyautogui
from time import sleep

for c in range(0, 200):
	sleep(3)
	pyautogui.hotkey('ctrl','t')
	sleep(2)
	pyautogui.write('https://www.youtube.com/watch?v=hgiLmZTlRp4')
	pyautogui.press('enter')
	sleep(7)
	pyautogui.hotkey('ctrl','w')
