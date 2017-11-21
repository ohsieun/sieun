import random

from pico2d import *

class Icon_planet:
    def __init__(self):
        self.image = load_image('small_planet_red.png')
        #                self.image = load_image('small_planet_yellow.png')
        #                self.image = load_image('small_planet_white.png')
        #                self.image = load_image('small_planet_blue.png')

    def draw(self):
        self.image.draw(30, 560)
    # fill here

#    def get_bb(self):
#        return 20, 20, 40, 40
#        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())