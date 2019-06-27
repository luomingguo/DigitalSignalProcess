import numpy as np
def F2T(f, sf):
    df = f[1] - f[0]
    Fmx = f[len(f)-1] - f[0] + df
    dt = 1 / Fmx
    N = len(sf)
    T = dt * N

    # t = 0:dt: T - dt;
    t = np.arange(0, T, dt)


    sff = np.fft.fftshift(sf)

    st = Fmx * np.fft.ifft(sff)

    return t, st
