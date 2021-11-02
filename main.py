import pygame
import json, os

#Initialize controller
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

# Read in key mappings
with open(os.path.join("ps4_keys_main.json"), 'r+') as file:
    button_keys = json.load(file)