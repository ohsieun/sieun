import random

from pico2d import *

class Item_booster:
    def __init__(self):
        self.image = load_image('item_booster.png')
#        self.x, self.y = 800, 100
        self.x, self.y = random.randint(800, 3200), 70
        self.move_speed = 50
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
        return self.x - 35, self.y - 35, self.x + 35, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())