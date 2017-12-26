import random

from pico2d import *

class Tree:
    def __init__(self):
        self.image = load_image('tree.png')
#        self.x, self.y = random.randint(800, 3200), 100
        self.x, self.y = random.randint(800, 1100), 200

#        self.move_speed = random.randint(20, 100)
        self.move_speed = 35
        self.dir = -1

    def update(self,frame_time):
        self.x -= frame_time * self.move_speed

        if self.x < -40:
            self.x = 850

    def draw(self):
        self.image.draw(self.x, self.y)
    # fill here

    def get_bb(self):
        return self.x - 60, self.y - 80, self.x + 60, self.y + 80

    def draw_bb(self):
        draw_rectangle(*self.get_bb())