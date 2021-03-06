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
    FRAMES_PER_ACTION = 2



    image = None
    eat_sound = None
    hurt_sound = None

    LEFT, RIGHT, UP, DOWN = 1, 0, 2, 3

    state_check = 0


    def __init__(self):
        self.x, self.y = 20, 90
#        self.frame = random.randint(0, 7)
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.RIGHT
        self.state_check = 0

        if Prince.image == None:
            Prince.image = load_image('prince_7.png')
        if Prince.eat_sound == None:
            Prince.eat_sound = load_wav('effect_eat.wav')
            Prince.eat_sound.set_volume(32)
        if Prince.hurt_sound == None:
            Prince.hurt_sound = load_wav('effect_crack.wav')
            Prince.hurt_sound.set_volume(32)


    def eat(self, item):
        self.eat_sound.play()

    def hurt(self, monster):
        self.hurt_sound.play()

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Prince.RUN_SPEED_PPS * frame_time
        self.total_frames += Prince.FRAMES_PER_ACTION * Prince.ACTION_PER_TIME * frame_time / 2

        self.frame = int(self.total_frames) % 2
#        self.handle_state[self.state](self)

        self.x += (self.dir * distance)*(2/3)

        self.x = clamp(0, self.x, 800)


        if self.state == self.UP:
            self.y = min(180, self.y + 90)
        elif self.state == self.DOWN:
#            self.y = max(0, self.y - 5)
            self.y = 90


    def draw(self):
    #    self.image.clip_draw(0,0,60,80,self.x,self.y)
         self.image.clip_draw(self.frame * 100, (self.state % 5) * 112, 100, 112, self.x, self.y)



    def get_bb(self):       #bb - bounding box
        if self.state in (self.LEFT, self.RIGHT):
            return self.x - 30, self.y - 50, self.x + 30, self.y + 50
        elif self.state in (self.UP, self.DOWN):
            return self.x - 40, self.y - 40, self.x + 40, self.y + 20
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.LEFT, self.RIGHT,self.DOWN, self.UP):
                self.state = self.LEFT
                self.dir = -1
                self.state_check = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.LEFT, self.RIGHT, self.DOWN, self.UP):
                self.state = self.RIGHT
                self.dir = 1
                self.state_check = 1

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT, self.LEFT, self.DOWN, self.UP):
                self.state = self.UP
                self.dir = 1
                self.state_check = 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.RIGHT, self.LEFT, self.UP):
                self.state = self.DOWN
                self.dir = 1
                self.state_check = 3



