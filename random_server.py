import numpy as np


class RandomServer:
    def get_message(self):
        return np.round(np.random.random() * 2 - 1, 2), np.round(np.random.random() * 2 - 1, 2)

