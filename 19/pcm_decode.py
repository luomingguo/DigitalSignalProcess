import numpy as np

def pcm_decode(inner, v):


    n = len(inner[0])
    step = np.zeros(8)
    slot = np.zeros(8)
    inner = inner.reshape(8,n//8,order='f')
    slot[0] = 0
    slot[1] = 32
    slot[2] = 64
    slot[3] = 128
    slot[4] = 256
    slot[5] = 512
    slot[6] = 1024
    slot[7] = 2048
    step[0] = 2
    step[1] = 2
    step[2] = 4
    step[3] = 8
    step[4] = 16
    step[5] = 32
    step[6] = 64
    step[7] = 128
    out = np.zeros(n//8)
    for i in range(n//8):
        ss = 2 * inner [0][i] - 1
        tmp = int(inner [1][i] * 4 + inner [2][i] * 2 + inner [3][i] + 1)
        st = slot[tmp]
        dt = (inner [4][i] * 8 + inner [5][i] * 4 + inner [6][i] * 2 + inner [7][i])*step[tmp-1] + 0.5 * step[tmp-1]
        out[i] = ss * (st + dt) / 4096 * v

    return out
