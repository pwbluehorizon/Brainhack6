import numpy as np


class DummyServer:
    def get_message(self):
        return np.round(np.random.random() * 2 - 1, 2)
