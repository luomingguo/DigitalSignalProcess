import numpy as np
def T2F(t, st): # (16000，）,(1,16000)
    dt=t[1]-t[0]
    T = t[-1]
    df=1/T
    N = len(st[0][:])
    # f = -N / 2 * df : df :N / 2 * df - df
    start = -N / 2 * df
    step = df
    end = N / 2 * df
    f = np.arange(start, end, step)  # (16000,)
    sf = np.fft.fft(st[0][:])  # (1,16000)
    sf = T / N * np.fft.fftshift(sf)

    return f, sf

