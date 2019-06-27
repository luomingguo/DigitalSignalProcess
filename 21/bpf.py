import numpy as np
from F2T import F2T


def bpf(f, sf, B1, B2):  # (3,) (1, 16000) ,9, 11

    df = f[1] - f[0]
    T = 1 / df
    n = len(f)
    hf = np.zeros((1, n))  #(1, 16000)

    # bf = np.arange(np.floor(B1 / df), np.floor(B2 / df)+0.1)
    # print(np.floor(B1 / df))  # 1799.0
    # print(np.floor(B2 / df))  # 2199.0
    bf = np.arange(np.floor(B1 / df), np.floor(B2 / df)+1)  # (400,)
    # bf = np.arange(np.floor(B1 / df), np.floor(B2 / df)+1).reshape((1,-1))  # (1, 400)
    bf1 = np.floor(n / 2) + bf  # (201,)
    bf2 = np.floor(n / 2) - bf  # (201,)

    hf[0][int(bf1[0]): int(bf1[-1])] = 1 / np.sqrt(2 * (B2 - B1))
    hf[0][int(bf2[0]): int(bf2[-1])] = 1 / np.sqrt(2 * (B2 - B1))
    j = np.complex(0, 1)
    s1 = hf
    s2 = sf
    s3 = np.exp(-j * 2 * np.pi * f * 0.1 * T)
    yf = hf[0] * sf * np.exp(-j * 2 * np.pi * f * 0.1 * T)

    return F2T(f, yf)

