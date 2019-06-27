import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import savefig

# 解决不支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题

"""信道参数"""
u1 = 0.5
u2 = 0.707
u3 = 0.5
Ts1 = 1
Ts2 = 8
r = 5
a = [1, 2, 3, 4, 5]

"""取样点"""
t1 = np.linspace(-2, 8, 1001)  # 1 * 1001
t2 = np.linspace(-3, 12, 1501)  # 1 * 1501

"""初始化"""
b1 = np.zeros((1, 1001))
b2 = np.zeros((1, 1501))

for i in range(r):
    b1 += np.array([a[i] * (np.heaviside(t1-i * Ts1, 1)-np.heaviside(t1 - (i+1) * Ts1, 1))])
    b2 += np.array([a[i] * (np.heaviside(t2-i * Ts2, 1)-np.heaviside(t2 - (i+1) * Ts2, 1))])

"""测试项"""
# print(b1.shape)  # 1 * 1001
# print(b1[0][600]) # 4.5 test right!
# print(b2.shape)  # 1 * 1501
# print(b2[0][900]) # 3.5 test tight!

a = np.append(np.zeros((1, 100), dtype=float), [b1[0][i] for i in range(len(t1)-100)]) * u2
n = np.append(np.zeros((1, 200), dtype=float), [b1[0][i] for i in range(len(t1)-200)]) * u3
v = u1 * b1


s1 = u1 * b1 + u2 * np.append(np.zeros((1, 100), dtype=float), [b1[0][i] for i in range(len(t1)-100)]) + \
     u3 * np.append(np.zeros((1, 200), dtype=float), [b1[0][i] for i in range(len(t1) - 200)])
s2 = u1 * b2 + u2 * np.append(np.zeros((1, 100), dtype=float), [b2[0][i] for i in range(len(t2)-100)]) +\
     u3 * np.append(np.zeros((1, 200), dtype=float), [b2[0][i] for i in range(len(t2) - 200)])

fig = plt.figure(12, figsize=(20, 10), dpi=98)
fig.add_subplot(221, title='Ts=1时的输入信号')
plt.plot(t1, b1[0])
plt.grid(linestyle='-.')
fig.add_subplot(222, title='Ts=1时输出信号')
plt.plot(t1, s1[0])
plt.grid(linestyle='-.')
fig.add_subplot(223, title='Ts=8时的输入信号')
plt.plot(t2, b2[0])
plt.grid(linestyle='-.')
fig.add_subplot(224, title='Ts=8时的输出信号')
plt.plot(t2, s2[0])
plt.grid(linestyle='-.')
plt.subplots_adjust(wspace=1, hspace=1)
fig.tight_layout()
plt.show()
fig.savefig("./2.jpg", dpi=98)
