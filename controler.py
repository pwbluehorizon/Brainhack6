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
    def calculate_speed_multiplier(bis_bas, arousal):
        if bis_bas > 0:
            if bis_bas < 6 - arousal:
                return 1.05
            else:
                return 1
        else:
            if bis_bas < - arousal:
                return 1.1
            else:
                return 0.95

    parameters['bis_bas'] = advice['bis_bas']
    parameters['arousal'] = advice['arousal']
    new_speed = np. round(parameters['speed'] * calculate_speed_multiplier(advice['bis_bas'], advice['arousal']), 2)
    parameters['speed'] = max(1, min(10, new_speed))
    parameters['enemies_frequency'] = 95 if advice['fire_up'] else int(advice['arousal'] * 2)


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
