import socket

import numpy as np


class Server:
    def __init__(self, ip='127.0.0.1', port=5412):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))
        
        self.last_value = 0
        self.tick = 0
    
    def get_message(self):
        if self.tick % 10 == 0:
            data = clear_buffer(self.sock)
            self.tick = 0
        else:
            data = self.last_value
        
        self.last_value = data
        self.tick += 1
        
        print(data)
        difference = str(data).split('\\t')
        
        return np.round(float(difference[0].strip("b'")), 2),\
            max(0, min(6, np.round(float(difference[1].strip("b'")), 2) + 3))


def clear_buffer(sock):
    try:
        previous_data = 0
        data, _ = sock.recvfrom(100)
        for i in range(5):
            previous_data = data
            data, _ = sock.recvfrom(100)
    except Exception as e:
        print(e)
    return previous_data