import numpy as np
from turtle import done
from turtle import ontimer

from cannon import move
from cannon import prepare_game_state


def prepare_parameters(configuration):
    return {
        'speed': 1,
        'enemies_frequency': 20,
    }


def get_server_message(server):
    return server.get_message()


def get_advice(game_state, parameters, server_message):
    return server_message #TODO


def update_parameters(advice, parameters):
    parameters['message'] = advice
    parameters['speed'] = np.mean(max(1, min(10, (advice + 1) * 3), parameters['speed']))
    parameters['enemies_frequency'] = max(2, int((advice + 1) * 30))


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
