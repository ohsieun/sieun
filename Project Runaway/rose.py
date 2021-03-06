import random

from pico2d import *

class Rose:
    def __init__(self):
        self.image = load_image('rose_in_the_bottle.png')
#        self.x, self.y = random.randint(800, 3200), 100
        self.x, self.y = random.randint(4000, 4100), 90

        self.move_speed = 35
        self.dir = -1

    def update(self,frame_time):
        self.x -= frame_time * self.move_speed


    def draw(self):
        self.image.draw(self.x, self.y)
    # fill here

    def get_bb(self):
        return self.x - 60, self.y - 80, self.x + 60, self.y + 80

    def draw_bb(self):
        draw_rectangle(*self.get_bb())