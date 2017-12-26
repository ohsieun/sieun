import random

from pico2d import *

class Dirty_water:
    def __init__(self):
        self.image = load_image('dirty_water.png')
#        self.x, self.y = 800, 100
        self.x, self.y = random.randint(800, 3200), 40
        self.move_speed = 60
        self.dir = -1

    def update(self,frame_time):
    #    self.frame = (self.frame + 1) % 8
#        self.frame = self.frame
        self.x -= frame_time * self.move_speed

#        if self.x < 0:
#            self.x = 800

    def draw(self):
        self.image.draw(self.x, self.y)
    # fill here

    def get_bb(self):
        return self.x - 70, self.y - 30, self.x + 70, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())