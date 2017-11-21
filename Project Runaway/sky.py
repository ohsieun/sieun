import random

from pico2d import *

class Sky:
    def __init__(self):
        self.image = load_image('sky.png')

    def draw(self):
        self.image.draw(480, 300)
    # fill here
