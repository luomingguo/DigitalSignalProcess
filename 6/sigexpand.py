
import numpy as np


def sigexpand(d, M):
    N = len(d[0])
    out = np.zeros((M, N))
    out[0,:] = d[0]
    out = out.reshape((1, -1), order='F')

    return out