import numpy as np
from nextpow2_2 import nextpow2

# def fftseq(m,ts,df):
def fftseq(*args):
    fs = 1 / args[1]
    if len(args) == 2:
        n1 = 0
    else:
        n1 = fs / args[2]

    n2 = len(args[0])
    n = 2 ** (max(nextpow2(n1), nextpow2(n2)))
    M = np.fft.fft(args[0], n)
    print("m",args[0].shape)
    m = np.hstack((args[0], np.zeros((1, n - n2))[0]))
    print("m2", m.shape)
    df = fs / n
    return M, m, df