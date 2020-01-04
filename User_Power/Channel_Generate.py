import numpy as np


def Channel_Generate(dis):
    h = 2 ** 0.5 / 2 * (np.random.randn(1, 1)) + 1j * (np.random.randn(1, 1)) * dis ** -2
    gh = np.linalg.norm(h)
    return gh
