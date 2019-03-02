from controler import run_game
from dummy_server import DummyServer


def get_server():
    return DummyServer()


if __name__ == '__main__':
    server = get_server()
    run_game(None, server)
    print('kwiatek')