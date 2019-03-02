"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange

from freegames import vector
from turtle import *


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

enemies_frequency = 40


def prepare_game_state(configuration):
    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    return None


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw(parameters):
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    goto(170, 190)
    write(parameters['message'])

    goto(140, 190)
    write(parameters['speed'])

    update()


def move(game_state, parameters):
    "Move ball and targets."
    if randrange(parameters['enemies_frequency']) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= parameters['speed']

    if inside(ball):
        speed.y -= 0.05
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw(parameters)

    for target in targets:
        if not inside(target):
            return
