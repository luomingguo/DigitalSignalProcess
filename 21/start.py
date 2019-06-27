import numpy as np
from sigexpand import sigexpand
import math
from T2F import T2F
from bpf import bpf
from matplotlib import pyplot as plt
# from scipy.ndimage import convolve
from scipy.signal import convolve
plt.rcParams['font.sans-serif'] = ['SimHei'] # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题

# 初始参数
M = 4
Ts = 1
fc = 10
N_sample = 16
N_num = 100

dt = 1 / fc / N_sample  # float:0.00625
t = np.arange(0, N_num * Ts, dt)  # (16000,)
t_num = len(t)
T = dt * len(t)  # 100.0

py1f = np.zeros((1, t_num), dtype=complex)
py2f = np.zeros((1, t_num), dtype=complex)

# d1 = np.sign(randn(1, N_num))
# 生成随机种子 1，可让每次输出结果与第一次随机得到的结果一致
# np.random.seed(0)
fig = plt.figure(1, figsize=(20,16), dpi=98)
# fig.add_subplot(221, xlabel="t", ylabel="QPS波形", title="经过带通后的波形")
# fig.add_subplot(222, xlabel="t", ylabel="OQPSK波形", title="经过带通后的波形")
for PL in range(100):

    d1 = np.sign(np.random.randn(1, N_num))  # (1,100)
    d2 = np.sign(np.random.randn(1, N_num))  # (1,100)
    gt = np.ones((1, fc * N_sample))  # (1, 160)

    s1 = sigexpand(d1[0], fc * N_sample)  # (1, 16000)
    s2 = sigexpand(d2[0], fc * N_sample)  # (1, 16000)

    #e % Press a key to see C vs. W and P/N0
    # k=[0.9,0.8,0.5,0.6]; b1 = np.convolve(np.ravel(s1), np.ravel(gt), mode='full').reshape((1, -1))  # (1, 16159)
    # b2 = np.convolve(np.ravel(s2), np.ravel(gt), mode='full').reshape((1, -1))  # (1, 16159)
    b1 = convolve(s1, gt).reshape((1, -1), order='f')  # (1, 16159)
    b2 = convolve(s2, gt).reshape((1, -1), order='f')  # (1, 16159)

    s3 = b1[:, :len(s1[0])]  # (1,16000)
    s4 = b2[:, :len(s2[0])]
    # st_qpsk = s1. * math.cos(2 * math.pi * fc * t) - s2. * math.sin(2 * math.pi * fc * t)
    st_qpsk = s3 * np.cos(2 * math.pi * fc * t) - s4 * np.sin(2 * math.pi * fc * t)  # (1, 16000)

    # s2_delay = [-ones(1, N_sample * fc / 2) s2(1:end - N_sample * fc / 2)];#有问题
    temp1 = -np.ones((1, N_sample * fc // 2)) #(1, 80)
    temp2 = s4[0][:len(s4) -1 - int(N_sample * fc / 2)].reshape((1,-1))  # (15920,)
    s2_delay = np.hstack((temp1[0], temp2[0])).reshape((1,-1))
    # st_oqpsk = s1. * cos(2 * pi * fc * t) - s2_delay. * sin(2 * pi * fc * t);
    st_oqpsk = s3 * np.cos(2 * np.pi * fc * t) - s2_delay * np.sin(2 * np.pi * fc * t)

    # 经过带通后， 在经过非线性电路
    f, y1f = T2F(t, st_qpsk)
    t1, y1 = bpf(f, y1f, fc - 1 / Ts, fc + 1 / Ts)  # (3,) (1, 16000) ,9, 11
    f, y2f = T2F(t, st_oqpsk)
    t2, y2 = bpf(f, y2f, fc - 1 / Ts, fc + 1 / Ts)  # (3,) (1, 16000) ,9, 11
    t1 = t1[:-1]
    t2 = t2[:-1]


    plt.subplot(221, xlabel="t", ylabel="OQPSK波形", title="经过带通后的波形")
    plt.plot(t1, y1)
    plt.xlim(5, 15)
    plt.ylim(-1.6, 1.6)
    plt.subplot(222, xlabel="t", ylabel="OQPSK波形", title="经过带通后的波形")

    plt.plot(t2, y2)
    plt.xlim(5, 15)
    plt.ylim(-1.6, 1.6)

    y1 = 1.5 * np.tanh(2 * y1).reshape((1,-1))
    y2 = 1.5 * np.tanh(2 * y2).reshape((1,-1))
    f3, y1f = T2F(t, y1)
    f4, y2f = T2F(t, y2)
    py1f += abs(y1f) ** 2 / T
    py2f += abs(y2f) ** 2 / T

py1f /= 100
py2f /= 100

fig.add_subplot(223, xlabel="f", ylabel="QPSK功率谱密度（dB/Hz)", title="经过非线性电路后的功率谱密度")

plt.plot(f3, 10 * np.log10(py1f[0]))
plt.xlim(-15, 15)
plt.ylim(-30, 10)


fig.add_subplot(224, xlabel="f", ylabel="OQPSK功率谱密度(dB/Hz)", title="经过非线性电路后的功率谱密度") # axis([-15 15 - 30 10]);
plt.plot(f4, 10 * np.log10(py2f[0]))
plt.xlim(-15, 15)
plt.ylim(-30, 10)
fig.savefig("./1.png")
plt.show()


plt.figure(2)
plt.subplot(111,title="非线性电路的输入输出函数")
x = np.arange(-2, 2+0.01, 0.1)
y = 1.5 * np.tanh(2 * x)

plt.plot(x, y)
plt.show()
