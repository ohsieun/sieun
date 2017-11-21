import random

from pico2d import *

class Blood_gage:
    def __init__(self):
        self.image = load_image('blood_gage_full_ex.png')
        #                self.image = load_image('blood_gage_empty.png')

    def draw(self):
        self.image.draw(330, 560)
    # fill here

#    def get_bb(self):
#        return 20, 20, 40, 40
#        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())