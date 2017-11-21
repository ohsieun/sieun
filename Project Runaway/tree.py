import random

from pico2d import *

class Tree:
    def __init__(self):
        self.image = load_image('tree.png')
        self.x, self.y = 430, 100

    def draw(self):
        self.image.draw(self.x, self.y)
    # fill here

    def get_bb(self):
        return self.x - 60, self.y - 80, self.x + 60, self.y + 80

    def draw_bb(self):
        draw_rectangle(*self.get_bb())