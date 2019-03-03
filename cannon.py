"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange

import matplotlib.pyplot as plt
from freegames import vector
from turtle import *


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

first_target_on_board = 0
game_state = {
    'enemies_number': 0,
    'score': 0,
    'strike': 0,
}


def prepare_game_state(configuration):
    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    return game_state


def tap(x, y):
    "Respond to screen tap."
    ball.x = -199
    ball.y = -199
    speed.x = (x + 200) / 27
    speed.y = (y + 200) / 27
    game_state['strike'] = 0


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def choose_color_based_on_bis_bas(bis_bas):
    cmap = plt.get_cmap('plasma')
    return cmap.colors[max(0, min(255, int((bis_bas + 3) / 6 * 256)))]


def draw(parameters, game_state):
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, target.color)

    if inside(ball):
        goto(ball.x, ball.y)
        dot(parameters['ball_radius'] * 2, 'red')

    goto(0, 190)
    write('{}:({})'.format(game_state['score'], game_state['strike']))

    goto(50, 190)
    write('S: {}'.format(parameters['speed']))

    goto(100, 190)
    write('BB: {}'.format(parameters['bis_bas']))

    goto(150, 190)
    write('A: {}'.format(parameters['arousal']))

    update()


def move(game_state, parameters):
    "Move ball and targets."
    if randrange(100) < parameters['enemies_frequency']:
        y = randrange(-150, 150)
        target = Target(200, y, choose_color_based_on_bis_bas(parameters['bis_bas']))
        targets.append(target)

    for target in targets:
        target.x -= parameters['speed']

    if inside(ball):
        speed.y -= 0.2
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        vectorized_target = vector(target.x, target.y)
        if abs(vectorized_target - ball) < 10 + parameters['ball_radius']:
            game_state['score'] += 100 + 100 * game_state['strike']
            game_state['strike'] += 1
        if not inside(target):
            game_state['score'] -= 50

        if abs(vectorized_target - ball) > 10 + parameters['ball_radius'] and inside(target):
            targets.append(target)

    game_state['enemies_number'] = len(targets)

    draw(parameters, game_state)

    for target in targets:
        if not inside(target):
            return


class Target(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    