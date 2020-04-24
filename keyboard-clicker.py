# clicker.py

import pynput
from pynput.keyboard import Key, Listener
from pynput.mouse import Controller, Button

# listen for keyboard events
# 2 phases: get button regions
# play back button regions

# example a b c d esc. captures mouse location on each keypress
# Then when a is pressed, make a click on that mouse location (same with b, c, d) until esc is pressed

mouse = pynput.mouse.Controller()

registered = {}  # associate key with location
saved_spots = {}


def register(key):
    print('registering', key)
    registered[key] = mouse.position


def press_spot(key):
    print('clicking spot with registered key', key)
    if key not in registered:
        return
    saved_spots[key] = mouse.position
    mouse.position = registered[key]
    mouse.click(button=Button.left)


def on_press(key):
    print('{0} pressed'.format(key))
    if key == Key.esc:
        exit(1)
    if key in registered:
        press_spot(key)
    else:
        register(key)


def on_release(key):
    print('{0} release'.format(key))
    if key in saved_spots:
        mouse.position = saved_spots[key]


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
