import numpy as np
import math
from matplotlib import pyplot as plt
from cm_sm52 import cm_sm52

plt.rcParams['font.sans-serif'] = ['SimHei'] # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题

def main():
    # np.arange与matlab的区别在于，前者end点小于15， 而matlab可以等于15
    SNRindB1 = np.arange(0, 15, 2)  # (8,)
    SNRindB2 = np.linspace(0, 15, 151, endpoint=True)  # (151,)
    # print(SNRindB1.shape) # (8,)

    smld_err_prb = np.zeros(len(SNRindB1))
    # print(smld_err_prb.shape) #(8,)
    for i in range(len(SNRindB1)):
        smld_err_prb[i] = cm_sm52(SNRindB1[i])  # 8*1
    # print(smld_err_prb) # [0.     0.     0.0001 0.     0.     0.     0.     0.    ]

    SN = len(SNRindB2)  # (151,)
    theo_err_prb = np.zeros(SN)
    for i in range(SN):
        SNR = np.exp(SNRindB2[i] * np.log(10) / 10)
        theo_err_prb[i] = (1/2) * np.exp(-SNR/2)
    print(theo_err_prb)


    fig = plt.figure(12, figsize=(13, 13), dpi=98)

    fig.add_subplot(211)
    plt.subplot(2, 1, 1, xlabel="SNRindB1", ylabel='smld_err_prb')
    plt.semilogy(SNRindB1, smld_err_prb, lw=2)

    fig.add_subplot(212)
    plt.subplot(2, 1, 2, xlabel="SNRindB2", ylabel='smld_err_prb')
    plt.semilogy(SNRindB2, theo_err_prb, lw=2)
    plt.subplots_adjust(wspace=1, hspace=1)
    fig.tight_layout()
    plt.show()
    fig.savefig("./2.png", dpi=98)

if __name__ == '__main__':
    main()