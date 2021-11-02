import pygame
from pynput.keyboard import Key, Controller
import json, os

running = True
keyboard = Controller()
pygame.init()

#Initialize controller
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

# Read in key mappings
with open(os.path.join("ps4_keys_main.json"), 'r+') as file:
    button_keys = json.load(file)


while running:

    for event in pygame.event.get():
        # Press Down On A Button
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['left_arrow']:
                keyboard.press('a')
                keyboard.release('a')
            if event.button == button_keys['right_arrow']:
                keyboard.press('d')
                keyboard.release('d')
            if event.button == button_keys['down_arrow']:
                keyboard.press('c')
                keyboard.release('c')
            if event.button == button_keys['up_arrow']:
                keyboard.press('b')
                keyboard.release('b')
            if event.button == button_keys['PS']:
                running = False
                print("FAIL SAFE")
        # Press Down On A Button
        if event.type == pygame.JOYBUTTONUP:
            pass