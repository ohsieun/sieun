import random

from pico2d import *

class Prince:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 20, 90
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.state = self.RIGHT_STAND
        if Prince.image == None:
#            Prince.image = load_image('prince_animation.png')
            Prince.image = load_image('prince_1.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Prince.RUN_SPEED_PPS * frame_time
        self.total_frames += Prince.FRAMES_PER_ACTION * Prince.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5
        self.x += (self.dir * distance)

        self.x = clamp(0, self.x, 800)


    def draw(self):
        self.image.clip_draw(0,0,60,80,self.x,self.y)
    #     self.image.clip_draw(self.frame * 100, self.state * 300, 100, 100, self.x, self.y)
    #        self.image.clip_draw(self.frame * 50, self.state * 50, 100, 100, self.x, self.y)
               #   clip_draw(left, bottom, width, height, x, y)

    def get_bb(self):       #bb - bounding box
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN):
                self.state = self.LEFT_RUN
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN):
                self.state = self.RIGHT_RUN
                self.dir = 1
#        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
#            if self.state in (self.UP_STAND, self.RIGHT_RUN, self.LEFT_RUN):
#                self.state = self.UP_RUN
#                self.dir =

#        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
#            if self.state in ():
#                self.state =
#                self.dir =

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
                self.dir = 0





