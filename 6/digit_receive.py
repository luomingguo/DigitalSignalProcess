import numpy as np
from sigexpand import sigexpand
from matplotlib import pyplot as plt
from scipy.signal import convolve
plt.rcParams['font.sans-serif'] = ['SimHei'] # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题

def digit_receive():
    N = 100

    N_sample = 8  # 每码元抽样点数
    Ts = 1
    dt = Ts / N_sample
    t = np.arange(0, N * N_sample  * dt, dt)

    T = 1
    gt = np.ones((1, N_sample))  # 数字基带波形
    d = np.sign(np.random.randn(1, N))  # 输入数字序列
    a = sigexpand(d, N_sample)
    st = convolve(a, gt) # 数字基带信号

    ht1 = gt
    rt1 = convolve(st, ht1)

    ht2 = 5 * np.sinc(5 * (t - 5) / Ts).reshape((1,-1))

    rt2 = convolve(st, ht2)

    fig = plt.figure(1, figsize=(15, 8), dpi=98)
    fig.add_subplot(321) # axis([0 20 - 1.5 1.5]);
    plt.subplot(3, 2, 1, xlabel="t", ylabel='输入双极性NRZ数字基带波形', title='输入双极性NRZ数字基带波形',)
    plt.plot(t, st[0][:len(t)],'bD-')
    plt.grid(linestyle='-.')
    plt.xlim(0, 20)
    plt.ylim(-1.5, 1.5)

    fig.add_subplot(322)
    plt.subplot(3, 2, 2,xlabel="t", ylabel='输入数字序列', title='输入数字序列')# axis([0 20 -1.5 1.5])
    plt.stem(t,a[0])
    plt.grid(linestyle='-.')
    plt.subplot(3, 2, 3, xlabel="t", ylabel='方波滤波后输出', title='方波滤波后输出')  # axis([0 20 -1.5 1.5])
    plt.plot(t, np.hstack((np.array(0),rt1[0][:len(t)-1] / 8 - 1)))
    plt.xticks(np.arange(0, 20, 1.5))
    plt.stem(t, a[0])

    plt.subplot(3, 2, 4, xlabel="t", ylabel='方波滤波后抽样输出', title='方波滤波后抽样输出')  # axis([0 20 -1.5 1.5])
    dd = rt1[0][N_sample:-1:N_sample].reshape((1,-1))

    ddd = sigexpand(dd, N_sample)

    plt.stem(t[:-1], ddd[0][:len(t)-1] / 8)
    plt.xlim(0, 20)
    plt.ylim(-1.5, 1.5)

    fig.add_subplot(325, ylabel='理想低通滤波后输出', xlabel='t/Ts')  # axis([0 20 - 1.5 1.5]);
    plt.xlim(0,20)
    plt.xlim(-1.5, 1.5)
    plt.plot(t-5, np.hstack((np.array(0),rt2[0][:len(t)-1] / 8 )))

    fig.add_subplot(326, ylabel='理想低通滤波后抽样输出', xlabel='t/Ts')
    dd = rt2[0][N_sample - 1: -1:N_sample].reshape((1,-1))
    print("dd", dd.shape)
    ddd = sigexpand(dd, N_sample)
    print("ddd",ddd.shape)
    plt.stem((t - 5)[:-1], ddd[0][:len(t)-1] / 8 )
    plt.xlim(0, 20)
    plt.xlim(-1.5, 1.5)
    plt.subplots_adjust(wspace=1, hspace=1)
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    digit_receive()