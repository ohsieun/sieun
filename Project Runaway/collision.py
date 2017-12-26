from pico2d import *

import game_framework

import title_state


from prince import Prince # import Prince class from prince.py

from rose import Rose

from sky import Sky
from grass import Grass

from icon_pause import Icon_pause
from icon_planet import Icon_planet
from blood_gage import Blood_gage

from tree import Tree
from tree2 import Tree2

from dirty_water import Dirty_water

from item_barrier import Item_barrier
from item_booster import Item_booster

name = "collision"

rose = None
prince = None
grass = None
icon_pause = None
icon_planet = None
blood_gage = None

tree = None
tree2 = None

trees = None
trees2 = None
sky = None
big_balls_for_collision_check = None
dirty_waters = None
item_barriers = None
item_boosters = None

def create_world():
    global prince,rose, sky, grass, balls, big_balls, icon_pause, icon_planet, blood_gage, tree, tree2, trees, trees2, dirty_waters, item_barriers, item_boosters
    prince = Prince()
    rose = Rose()
    icon_pause = Icon_pause()
    icon_planet = Icon_planet()
    blood_gage = Blood_gage()
    tree = Tree()
    tree2 = Tree2()
#    trees = [Tree() for i in range(5)]
#    trees2 = [Tree2() for i in range(5)]
    dirty_waters = [Dirty_water() for i in range (2)]
    item_barriers = [Item_barrier() for i in range (3)]
    item_boosters = [Item_booster() for i in range (3)]


#    big_balls = [BigBall() for i in range(10)]

#    big_balls_for_collsion_check = big_balls, []


#    balls = [Ball() for i in range(10)]
#    balls = big_balls + balls
    grass = Grass()
    sky = Sky()


def destroy_world():
    global prince, grass, balls, big_balls, icon_pause, icon_planet, blood_gage, trees, tree2, trees2, dirty_waters,item_barriers, item_boosters

    del(prince)
    del(rose)
    del(icon_pause)
    del(icon_planet)
    del(blood_gage)

    del(tree)
    del(tree2)
#    del(trees)
#    del(trees2)
    del(dirty_waters)
    del(item_barriers)
    del(item_boosters)

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
            if event.type == SDL_MOUSEMOTION:
                x, y = event.x, 600 - event.y

#                if x >
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

    tree.update(frame_time)
    tree2.update(frame_time)
#    for tree in trees:
#        tree.update(frame_time)

#    for tree2 in trees2:
#        tree2.update(frame_time)

    for dirty_water in dirty_waters:
        dirty_water.update(frame_time)

    for item_booster in item_boosters:
        item_booster.update(frame_time)

    for item_barrier in item_barriers:
        item_barrier.update(frame_time)


    prince.update(frame_time)
    rose.update(frame_time)
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

    for item_booster in item_boosters:
        if collide(prince, item_booster):
            item_boosters.remove(item_booster)
            prince.eat(item_booster)

    for item_barrier in item_barriers:
        if collide(prince, item_barrier):
            item_barriers.remove(item_barrier)
            prince.eat(item_barrier)

    for dirty_water in dirty_waters:
        if collide(prince, dirty_water):
            prince.hurt(dirty_water)


    if collide(prince, tree):
        prince.hurt(tree)


    if collide(prince, tree2):
        prince.hurt(tree2)

def draw(frame_time):
    clear_canvas()
    sky.draw()

    icon_pause.draw()
    icon_planet.draw()
    blood_gage.draw()

    grass.draw()

    tree.draw()
    tree2.draw()
#    for tree in trees:
#        tree.draw()

#    for tree2 in trees2:
#        tree2.draw()

    for dirty_water in dirty_waters:
        dirty_water.draw()

    for item_barrier in item_barriers:
        item_barrier.draw()

    for item_booster in item_boosters:
        item_booster.draw()

    rose.draw()
    prince.draw()

#    grass.draw_bb()
#    tree.draw_bb()
#    tree2.draw_bb()
#    prince.draw_bb()

#    for item_booster in item_boosters:
#        item_booster.draw_bb()

#    for item_barrier in item_barriers:
#        item_barrier.draw_bb()

 #   for dirty_water in dirty_waters:
 #       dirty_water.draw_bb()

    update_canvas()






