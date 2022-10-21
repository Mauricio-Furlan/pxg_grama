from time import sleep
import button
import keyboard
import pyautogui

right = (1035,508,50,50)
left = (850,508,50,50)
top = (944,415,50,50)
bot = (943,600,50,50)

list_positions = [right, left, top, bot]

def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

def get_bush(location):
  if location != None:
    move(location)
    keyboard.press(button.key['BACKSPACE'], 0.5)
    pyautogui.click()
    sleep(4)

def move_and_click(location):
  move(location)
  pyautogui.click()

for index in range(7):
  while True:
    position_in_map = pyautogui.locateOnScreen('./flags/flag_{}.png'.format(index), confidence=0.80)
    print(position_in_map)
    if position_in_map != None:
      move_and_click(position_in_map)
      sleep(6.5)
      check_position = pyautogui.locateOnScreen('./flags/flag_{}.png'.format(index), confidence=0.80)
      if check_position == None:
        for position in list_positions:
          for index in range(3):
            bush = pyautogui.locateOnScreen('bushs/bush_{}.PNG'.format(index), confidence=0.85, region=position)
            get_bush(bush)
        break
