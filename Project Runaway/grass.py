import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('land_red.png')

    def draw(self):
        self.image.draw(400, 30)
    # fill here

    def get_bb(self):
        return 0, 0, 800, 95
#        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())