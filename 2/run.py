
import numpy as np
from h import entropy2
from f import il3_8fun
from y import Q
from scipy import integrate
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题

def main():
    a_db = np.arange(-13, 13+0.1, 0.5)

    c_soft = np.zeros(53)
    a = 10 ** (a_db / 10)
    c_hard = np.zeros(53)
    tolerance=1e-3

    for i in range(53):
        c_hard[i] = 1 - entropy2(Q(a[i]))
        f, error = integrate.quad(il3_8fun, a[i] - 5, a[i] + 5, epsabs=tolerance, args=(a[i]))
        g, errr = integrate.quad(il3_8fun, -a[i] - 5, -a[i] + 5, epsabs=tolerance, args=(-a[i]))
        c_soft[i] = 0.5 * f + 0.5 * g



    fig = plt.figure(21, figsize=(13, 8), dpi=98)
    fig.add_subplot(211)
    plt.subplot(2, 1, 1, xlabel="S N R i n d B 1", ylabel='smld_err_prb')
    plt.semilogx(a, c_soft, lw=2)
    plt.grid()
    fig.add_subplot(212)
    plt.subplot(2, 1, 2, xlabel="SNRindB2", ylabel='theo_err_prb')
    plt.semilogx(a, c_hard)
    plt.grid()
    plt.subplots_adjust(wspace=1, hspace=1)
    fig.tight_layout()
    plt.show()
    fig.savefig("./2.png", dpi=98)

if __name__ == '__main__':
    main()