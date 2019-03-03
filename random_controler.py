from controler import run_game
from random_server import RandomServer


def get_server():
    return RandomServer()


if __name__ == '__main__':
    server = get_server()
    run_game(None, server)
