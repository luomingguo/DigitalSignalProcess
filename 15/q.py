import math
import numpy as np

# def q(x):
#     return np.array([(1/2) * math.erfc(x[i] / np.sqrt(2)) for i in range(len(x))])


def q(x):
    return (1/2) * math.erfc(x / np.sqrt(2))