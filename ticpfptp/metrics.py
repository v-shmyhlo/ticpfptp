import numpy as np


class Mean(object):
    def __init__(self):
        self.values = []

    def compute(self):
        return sum(self.values) / len(self.values)

    def update(self, value):
        values = np.array(value).flatten()
        self.values.extend(values)

    def reset(self):
        self.values = []

    def compute_and_reset(self):
        value = self.compute()
        self.reset()
        return value
