import math
import numpy as np

def q(x):
    return np.array([(1/2) * math.erfc(x[i] / np.sqrt(2)) for i in range(len(x))])