import numpy as np


class DummyServer(object):
    
    def get_message(self) -> float:
        return np.random()*2 -1
    
    
print(DummyServer)