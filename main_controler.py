from controler import run_game
from server import Server


def get_server():
    return Server()


if __name__ == '__main__':
    server = get_server()
    run_game(None, server)

