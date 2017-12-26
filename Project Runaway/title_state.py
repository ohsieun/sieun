import game_framework
import collision
from pico2d import *

name = "TitleState"
image = None

def enter():
    global image
    image = load_image('title_1.png')

def exit():
    global image
    del(image)


def handle_events(frame_time):
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(collision)
def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update(frame_time):
   # if not running:
   #   game_framework.quit()       # start_state의 resume 수행..?
    pass


def pause():
    pass


def resume():
    pass