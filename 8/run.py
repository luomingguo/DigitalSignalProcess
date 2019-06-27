import  numpy as np
import matplotlib.pyplot as plt
from scipy.special import sinc
from scipy.fftpack import fft, fftshift
def run():

    n = np.arange(-20, 21,1)
    x = 0.5 * (sinc(n / 2)) ** 2
    print("x", x.shape)
    fig1 = plt.figure(1, figsize=(15, 8), dpi=98)
    fig1.add_subplot(211)
    plt.subplot(211, xlabel="n", ylabel="y")
    plt.grid("-.")
    plt.plot(n, x)
    plt.ylim(0, 0.6)

    plt.subplot(212, xlabel="n", ylabel="y")
    plt.stem(n, x)
    plt.ylim(0, 0.6)


    ts = 1/40
    fig2 = plt.figure(2, figsize=(15, 8), dpi=98)
    fig2.add_subplot(111)
    plt.subplot(111)
    t = np.arange(-0.5, 1.5  , ts)
    print("t", t.shape)
    fs = 1 / ts
    b = np.hstack((np.zeros((1, 20))[0], t[20:60], np.zeros((1, 20))[0]))
    print("b", b.shape)
    H = fft(b)/fs
    print("H", H.shape)
    df = fs/80
    f = np.arange(0, fs , df) - fs / 2
    print("f", f.shape)
    plt.plot(b, f)
    H1 = fftshift(H)
    print("H1", H1.shape)
    y = x * H1[19:60]


    fig3 = plt.figure(3, figsize=(15, 8), dpi=98)
    fig3.add_subplot(111)
    plt.subplot(111)
    plt.stem(n, y,linefmt='r-', basefmt='r-',markerfmt='C3.')
    plt.ylim(-0.2, 0.3)
    fig1.savefig("./1.png")
    fig2.savefig("./2.png")
    fig3.savefig("./3.png")
    plt.show()


if __name__ == '__main__':
    run()