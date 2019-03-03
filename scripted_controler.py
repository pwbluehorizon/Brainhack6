from controler import run_game
from scripted_server import ScriptedServer


def get_server():
    return ScriptedServer()


if __name__ == '__main__':
    server = get_server()
    run_game(None, server)
