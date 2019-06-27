import math
import random
import numpy as np
from gngauss import gngauss


def cm_sm52(snr_in_dB):

    N = 10000
    Eb = 1
    d = 1
    snr = 10 ** (snr_in_dB / 10)  # 每一比特的信噪比
    sgma = np.sqrt(Eb / (2 * snr))  # 信噪比方差
    phi = 0
    numoferr = 0
    dsource = np.zeros(10000)

    for i in range(N):
        if (random.random() < 0.5):
            dsource[i] = 0
        else:
            dsource[i] = 1

    for i in range(N):

        if (dsource[i] == 0):
            r0c = np.sqrt(Eb) * np.cos(phi) + gngauss(0, sgma)
            r0s = np.sqrt(Eb) * np.sin(phi) + gngauss(0, sgma)
            r1c = gngauss(0, sgma)
            r1s = gngauss(0, sgma)

        else:
            r0c = gngauss(0, sgma)
            r0s = gngauss(0, sgma)
            r1c = np.sqrt(Eb) * np.cos(phi) + gngauss(0, sgma)
            r1s = np.sqrt(Eb) * np.sin(phi) + gngauss(0, sgma)

        # square law detector outputs 平方检测输出法？
        r0 = r0c ** 2 + r0s ** 2
        r1 = r1c ** 2 + r1s ** 2

        if r0 > r1:
            decis = 0
        else:
            decis = 1

        # 如果检测错误，记录错误
        if (decis != dsource[i]):
            numoferr = numoferr + 1

        return numoferr / N
