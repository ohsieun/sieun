import random

from pico2d import *

class Blood_gage:
    font = None
    advanced_time = None

    def __init__(self):
        self.image = load_image('blood_gage_full_ex.png')
        if Blood_gage.font == None:
            Blood_gage.font = load_font('ENCR10B.TTF', 16)

    def draw(self):
        self.image.draw(330, 560)
        self.font.draw(600, 560, 'Time: %3.2f' % get_time(), (255, 255, 0))
    # fill here

    def update(self):
        print("Change Time: %f" %
              (get_time()))
        print(advanced_time = get_time())
        if('advanced_time' == 10):
            return False

        pass
#    def get_bb(self):
#        return 20, 20, 40, 40
#        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

#    def draw_bb(self):
#        draw_rectangle(*self.get_bb())