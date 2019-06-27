import matplotlib.pyplot as plt
import math
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题

"""横坐标取样列表"""

x = np.linspace(-1, 1, 300, endpoint=False)
"""信道参数"""
u1 = 0.5
u2 = 0.707
u3 = 0.5
τ1 = 0
τ2 = 1
τ3 = 2
j = complex(0, 1)


f = [abs(u1 * math.e **(-j*2*math.pi*τ1*x[i]) + u2 * math.e **(-j*2*math.pi*τ2*x[i])+ \
    u3 * math.e ** (-j*2*math.pi*τ3*x[i])) for i in range(300)]
s = [(u1 * math.e ** (-j * 2 * math.pi * τ1* x[i]) + u2 * math.e **(-j*2*math.pi*τ2*x[i])+ \
    u3 * math.e ** (-j*2*math.pi*τ3*x[i])) for i in range(300)]

fig = plt.figure(12,figsize=(13,8),dpi=98)
fig.add_subplot(211, xlabel="ω / π", ylabel='|H(2πf)|', title='幅频特性', )
plt.plot(2*x, f)
plt.grid(linestyle='-.')
fig.add_subplot(212, xlabel="ω / π", ylabel='θ(2πf)', title='相频特性')
plt.plot(2*x, np.angle(s))
plt.grid(linestyle='-.')
plt.subplots_adjust(wspace =1, hspace =0.5)
fig.tight_layout()
plt.show()
fig.savefig("./1.png", dpi=98)




