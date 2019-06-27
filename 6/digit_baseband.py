import numpy as np
from sigexpand import sigexpand
from scipy.special import sinc
from scipy.signal import convolve
from T2F import T2F
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei'] # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题

# 数字基带信号的功率谱密度
def digit_baseband():

    Ts = 1
    N_sample = 8  # 每个码元的抽样点数
    dt = Ts / N_sample # 抽样时间间隔
    N = 1000  # 码元数
    T =1
    t = np.arange(0, N * N_sample * dt, dt)

    gt1 = np.ones((1, N_sample)) # NRZ非归零波形

    gt2 = np.ones((1, N_sample // 2)) # RZ归零波形

    gt2 = np.hstack((gt2, np.zeros((1, N_sample // 2))))

    mt3 = sinc((t - 5) / Ts).reshape(1,-1)  #  sin(pi * t / Ts) / (pi * t / Ts)

    gt3 = mt3[0:10 * N_sample].reshape((1,-1))

    d = (np.sign(np.random.randn(1, N)) + 1) / 2

    data = sigexpand(d, N_sample)  # 对序列间隔插入N_sample - 1个0



    st1 = convolve(data, gt1)

    st2 = convolve(data, gt2)

    d = 2 * d - 1 #变成双极性序列

    data = sigexpand(d, N_sample)

    st3 = convolve(data, gt3)


    f1, st1f = T2F(t, st1[:len(t)])

    f2, st2f = T2F(t, st2[:len(t)])

    f3, st3f = T2F(t, st3[:len(t)])

    fig1 = plt.figure(1, figsize=(13, 8), dpi=98)
    fig1.add_subplot(321)
    plt.subplot(3,2,1, ylabel='单极性NRZ波形')
    plt.xlim(0,20)  # axis([0 20 - 1.5 1.5]);
    plt.ylim(-2,2)  # axis([0 20 - 1.5 1.5]);
    plt.grid("-.")

    plt.plot(t, st1[0][:len(t)] )

    fig1.add_subplot(322)
    plt.grid("-.")
    plt.xlim(-5, 5)  # axis([0 20 - 1.5 1.5]);
    plt.ylim(-40, 10)
    plt.plot(f1, 10 * np.log10(abs(st1f) ** 2 / T))

    fig1.add_subplot(323,ylabel='单极性RZ波形')
    plt.grid("-.")
    plt.xlim(0, 20)
    plt.ylim(-1.5, 1.5)
    plt.plot(t, st2[0][:len(t)])


    fig1.add_subplot(324,ylabel='单极性RZ功率谱密度(dB/Hz)')
    plt.grid("-.")
    plt.xlim(-5, 5)
    plt.ylim(-40, 10)
    plt.plot(f2, 10 * np.log10(abs(st2f) ** 2 / T))

    fig1.add_subplot(325, ylabel='双极性sinc波形', xlabel='t/Ts')

    plt.plot(t - 5, st3[0][: len(t)])
    plt.grid("-.")
    plt.xlim(0, 20)
    plt.ylim(-2, 2)


    fig1.add_subplot(326, ylabel='sinc波形功率谱密度(dB/Hz)', xlabel='f*Ts')
    plt.grid("-.")
    plt.xlim(-5, 5)
    plt.ylim(-40, 10)
    plt.plot(f3[:-1], 10 * np.log10(abs(st3f) ** 2 / T))
    plt.show()


if __name__ == '__main__':
    digit_baseband()