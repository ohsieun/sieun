import game_framework
import collision

from pico2d import *

name = "TitleState"
image1 = None
image2 = None

def enter():
    global image1, image2
    image1 = load_image('title_1.png')
    image2 = load_image('title_2.png')

def exit():
    global image1,image2
    del(image1)
    del(image2)


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
    global image
    clear_canvas()
    image1.draw(400, 300)
    image2.draw(400,100)
    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass