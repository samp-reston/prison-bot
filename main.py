from keyboard import press, press_and_release, release, write
from mouse import move, _mouse_event, click, get_position
import time
import pywinauto
import cv2
import numpy as np


HORIZONTAL_WALKING_SPEED = 3.9  # Blocks per second

VERTICAL_FLYING_SPEED = 7.49  # Blocks per second
HORIZONTAL_FLYING_SPEED = HORIZONTAL_WALKING_SPEED * 2.5  # Blocks per second

MINE_WIDTH = 31  # Blocks
MINE_HEIGHT = 39  # Calculate this at some point

# Seconds to move 39 blocks vertically
VERTICAL_TIME = MINE_HEIGHT / VERTICAL_FLYING_SPEED

# Seconds to move 31 blocks horizontally
HORIZONTAL_TIME = MINE_WIDTH / HORIZONTAL_WALKING_SPEED


def reset_mine():
    press_and_release('/')
    time.sleep(0.1)
    write('mine reset')
    press_and_release('enter')
    time.sleep(0.1)
    move(0, 100, False, 0.1)


def move_left(weight=1.0):
    press("a")
    time.sleep(HORIZONTAL_TIME * weight)
    release("a")


def move_right(weight=1.0):
    press("d")
    time.sleep(HORIZONTAL_TIME * weight)
    release("d")


def move_forward(weight=1.0):
    press("w")
    time.sleep(HORIZONTAL_TIME * weight)
    release("w")


def move_back(weight=1.0):
    press("s")
    time.sleep(HORIZONTAL_TIME * weight)
    release("s")


def move_player(direction):
    if direction == "left":
        move_left()
    elif direction == "right":
        move_right()
    elif direction == "back":
        move_forward()
    elif direction == "forward":
        move_back()
    else:
        print("Invalid direction")


def move_forward_right(weight=1.0):
    press("w+d")
    time.sleep(HORIZONTAL_TIME * weight)
    release("w+d")


def calculate_mine_dimensions():
    move_forward_right()
    time_at_top_right = time.time()
    move_back()
    time_at_bottom_right = time.time()
    move_left()
    time_at_bottom_left = time.time()
    move_forward()
    time_at_top_left = time.time()

    top_right_to_bottom_right = time_at_bottom_right - time_at_top_right
    bottom_right_to_bottom_left = time_at_bottom_left - time_at_bottom_right
    bottom_left_to_top_left = time_at_top_left - time_at_bottom_left

    print(top_right_to_bottom_right, bottom_right_to_bottom_left, bottom_left_to_top_left)


def init():
    app = pywinauto.Application().connect(title_re="Minecraft")
    app.top_window().set_focus()
    press_and_release('esc')

    reset_mine()

    calculate_mine_dimensions()


init()
print("Done")
