import numpy as np
import math
import matplotlib.pyplot as plt


EbN0dB = np.arange(0, 10.1, 0.5)

N0=10 ** (-EbN0dB/10)
sigma=np.sqrt(N0/2)
# 理论结算的误码率
Pb=np.array([0.5*math.erfc(np.sqrt(1/N0[i])) for i in range(len(EbN0dB))])
# 仿真误码率
ber = np.zeros(len(EbN0dB))
for i in range(len(EbN0dB)):
    a=np.sign(np.random.randn(1,100000))   # 产生等概信源+1，-1
    rk= a[0] + sigma[i]*np.random.randn(1,100000)    # 离散等效接受模型
    dec_a=np.sign(rk)                      # 判决
    ber[i]=sum( abs(a[0]-dec_a[0])/2)/len(a[0])  # 计算误码率

plt.semilogy(EbN0dB,Pb)

plt.semilogy(EbN0dB,ber,'rd-')
plt.legend('理论值','仿真结果')
plt.xlabel('Eb/N0(dB)')
plt.ylabel('Pb')
plt.show()