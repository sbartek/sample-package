import numpy as np


class NormalNumberGenerator:

    def __init__(self, seed=None):
        if seed is not None:
            np.random.seed(seed=seed)

    def generate(self):
        return np.random.normal()
