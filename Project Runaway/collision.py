from pico2d import *

import game_framework


from prince import Prince # import Prince class from prince.py

from sky import Sky
from icon_pause import Icon_pause
from grass import Grass
from icon_planet import Icon_planet
from blood_gage import Blood_gage
from tree import Tree


name = "collision"


prince = None
grass = None
icon_pause = None
icon_planet = None
blood_gage = None
tree = None

sky = None
big_balls_for_collision_check = None

def create_world():
    global prince, sky, grass, balls, big_balls, icon_pause, icon_planet, blood_gage, tree
    prince = Prince()
    icon_pause = Icon_pause()
    icon_planet = Icon_planet()
    blood_gage = Blood_gage()
    tree = Tree()

#    big_balls = [BigBall() for i in range(10)]

#    big_balls_for_collsion_check = big_balls, []


#    balls = [Ball() for i in range(10)]
#    balls = big_balls + balls
    grass = Grass()
    sky = Sky()


def destroy_world():
    global prince, grass, balls, big_balls, icon_pause, icon_planet, blood_gage, tree

    del(prince)
    del(icon_pause)
    del(icon_planet)
    del(blood_gage)

    del(tree)

#    del(balls)
    del(grass)
    del(big_balls)
    del(sky)



def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                prince.handle_event(event)



def collide(a, b):          # a와 b는 객체. 무엇이든 상관 ㄴ
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update(frame_time):
    prince.update(frame_time)
#    for ball in balls:
#        ball.update(frame_time)

#    for ball in balls:
#        if collide(boy, ball):
#            balls.remove(ball)

#    for ball in big_balls_for_collision_check:
#        if collide(grass, ball):
#            ball.stop()
#            big_balls_for_collision_check.remove(ball)

#    delay(1.0)


def draw(frame_time):
    clear_canvas()
    sky.draw()

    icon_pause.draw()
    icon_planet.draw()
    blood_gage.draw()

    grass.draw()
    tree.draw()
    prince.draw()
#    for ball in balls:
#        ball.draw()

    grass.draw_bb()
    tree.draw_bb()
    prince.draw_bb()
#    for ball in balls:
#        ball.draw_bb()

    update_canvas()






