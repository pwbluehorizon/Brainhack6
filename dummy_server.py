class DummyServer:
    def __init__(self):
        self.tick = 0
        self.tick_numbers = 10
        self.tick_epoch = 12

    def get_message(self):
        self.tick += 1

        if self.tick <= self.tick_numbers * self.tick_epoch:
            return -3 + (self.tick // self.tick_numbers) * 0.5

        value = 3 - ((self.tick - self.tick_numbers * self.tick_epoch) // self.tick_numbers) * 0.5
        if self.tick == self.tick_numbers * self.tick_epoch * 2:
            self.tick = 0

        return value
