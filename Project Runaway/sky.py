import random

from pico2d import *

class Sky:
    def __init__(self):
        self.image = load_image('sky_red_1.png')
        self.bgm = load_music('MitiS - 1.16.2016.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(480, 300)
    # fill here
