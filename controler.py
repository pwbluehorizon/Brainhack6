import numpy as np
from turtle import done
from turtle import ontimer

from cannon import move
from cannon import prepare_game_state


def prepare_parameters(configuration):
    return {
        'speed': 1,
        'enemies_frequency': 20,
        'ball_radius': 3,
    }


def get_server_message(server):
    return server.get_message()


def get_advice(game_state, parameters, server_message):
    advice = {
        'fire_up': False,
        'bis_bas': server_message[0],
        'arousal': server_message[1],
    }
    if game_state['enemies_number'] < 1:
        advice['fire_up'] = True

    return advice


def update_parameters(advice, parameters):
    parameters['message'] = advice['arousal']
    parameters['speed'] = max(1, min(10, (max(0,(advice['arousal']+2))*2)))
    parameters['enemies_frequency'] = 95 if advice['fire_up'] else int(((2 + advice['arousal']) ) * 3)


def run_game(configuration, server):
    game_state = prepare_game_state(configuration)
    parameters = prepare_parameters(configuration)

    game_turn(game_state, parameters, server)
    done()


def game_turn(game_state, parameters, server):
    server_message = get_server_message(server)
    advice = get_advice(game_state, parameters, server_message)
    update_parameters(advice, parameters)

    move(game_state, parameters)

    ontimer(lambda: game_turn(game_state, parameters, server), 50)
