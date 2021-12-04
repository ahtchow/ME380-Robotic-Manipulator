import pygame
from pynput.keyboard import Key, Controller
import json, os
import time

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

key_mappings = {
    "x": 'f',
    "circle": 'h',
    "square": 'g',
    "triangle": 'e',
    "L1": 'i',
    "R1": 'j',
    "up_arrow": 'c',
    "down_arrow": 'd',
    "left_arrow": 'a',
    "right_arrow": 'b',
    "options": 'x'
}

keys_pressed = {}
for k in button_keys:
    keys_pressed[k] = False

if __name__ == "__main__":

    running = True
    while running:

        for event in pygame.event.get():
            # Press Down On A Button
            if event.type == pygame.JOYBUTTONDOWN:

                # Motor 0
                if event.button == button_keys['left_arrow']:
                    keys_pressed['left_arrow'] = True
                if event.button == button_keys['right_arrow']:
                    keys_pressed['right_arrow'] = True

                # Motor 1
                if event.button == button_keys['down_arrow']:
                    keys_pressed['down_arrow'] = True
                if event.button == button_keys['up_arrow']:
                    keys_pressed['up_arrow'] = True

                # Motor 2
                if event.button == button_keys['triangle']:
                    keys_pressed['triangle'] = True
                if event.button == button_keys['x']:
                    keys_pressed['x'] = True

                # Motor 3
                if event.button == button_keys['circle']:
                    keys_pressed['circle'] = True
                if event.button == button_keys['square']:
                    keys_pressed['square'] = True

                # Motor 4
                if event.button == button_keys['L1']:
                    keys_pressed['L1'] = True
                if event.button == button_keys['R1']:
                    keys_pressed['R1'] = True

                # Callibration
                if event.button == button_keys['options']:
                    keys_pressed['options'] = True

                # Safety Fail
                if event.button == button_keys['PS']:
                    running = False
                    print("FAIL SAFE")
            
            if event.type == pygame.JOYBUTTONUP:
                if event.button == button_keys['left_arrow']:
                    keys_pressed['left_arrow'] = False
                if event.button == button_keys['right_arrow']:
                    keys_pressed['right_arrow'] = False

                if event.button == button_keys['down_arrow']:
                    keys_pressed['down_arrow'] = False
                if event.button == button_keys['up_arrow']:
                    keys_pressed['up_arrow'] = False

                if event.button == button_keys['triangle']:
                    keys_pressed['triangle'] = False
                if event.button == button_keys['x']:
                    keys_pressed['x'] = False

                if event.button == button_keys['square']:
                    keys_pressed['square'] = False
                if event.button == button_keys['circle']:
                    keys_pressed['circle'] = False

                if event.button == button_keys['R1']:
                    keys_pressed['R1'] = False
                if event.button == button_keys['L1']:
                    keys_pressed['L1'] = False

                if event.button == button_keys['options']:
                    keys_pressed['options'] = False
        
        # Press the command based on status of controller
        for k in keys_pressed:
            if keys_pressed[k] == True:
                keyboard.press(key_mappings[k])
                keyboard.press(Key.enter)
                keyboard.release(key_mappings[k])
                keyboard.release(Key.enter)
        
        # Time delay to prevent command queue overload
        time.sleep(0.20)