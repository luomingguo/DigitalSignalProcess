
import numpy as np
import matplotlib.pyplot as plt
from pcm_encode import pcm_encode
from pcm_decode import pcm_decode

plt.rcParams['font.sans-serif'] = ['SimHei'] # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题
t = np.arange(0,10.01, 0.01)
vm1 = np.arange(-70,1)
vm = 10 ** (vm1 / 20)
fig = plt.figure(1, figsize=(13, 8), dpi=98)
fig.add_subplot(211, title="样本序列")
plt.grid()
snrq = np.zeros(len(vm))

for k in range(len(vm)):
    for m in range(2):
        x = vm[k] * np.sin(2 * np.pi * t + 2 * np.pi * np.random.rand(1))
        v = 1
        xx = x / v
        sxx = np.floor(xx * 4096)
        y = pcm_encode(sxx)
        yy = pcm_decode(y, v)

        nq = sum((x - yy)* (x - yy)) / len(x)
        sq = np.mean(yy **  2)
        snr = sq / nq

        plt.plot(t, x)
        plt.subplot(212,title='pcm 解码序列')
        plt.plot(t, yy)

    snrq[k] = 10 * np.log10(np.mean(snr))


plt.subplot(212)
plt.plot(vm1,snrq)
plt.xlim(-60, 0)


plt.grid()
plt.show()

