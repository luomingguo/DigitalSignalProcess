import numpy as np
from q import q
from BDT_INT2 import bdt_int2
from scipy import integrate
np.set_printoptions(suppress=True)
# 初始信噪比
initial_snr = 0
# 最终信噪比
final_snr = 12
# 信噪比增长步长
snr_step = 1
# Tolerance used for the integration 用于抵消集成的容差量
tolerance = 2.2204e-016
plus_inf = 20

snr_in_dB = np.arange(initial_snr, final_snr+0.1*snr_step, snr_step)

# 初始化
n = len(snr_in_dB)
Pe_2 = np.zeros(n)
Pe_4 = np.zeros(n)
Pe_8 = np.zeros(n)
Pe_16 = np.zeros(n)
Pe_32 = np.zeros(n)

for i in range(n):
    # snr=10^(snr_in_dB(i)/10);
    snr = 10 ** (snr_in_dB[i] / 10)

    Pe_2[i] = q(np.sqrt(snr))

    """           
    由于函数return回的结果有两个，其实是一个元祖，python语法中元祖不能直接乘以非int类型，因此前面系数
    在后面输出
    Pe_4[i], error = (2/3) *integrate.quad(bdt_int2, minus_inf, plus_inf,
                                    epsabs=tolerance, args=(snr, 4))"""
    Pe_4[i], error = integrate.quad(bdt_int2, 0, plus_inf, \
                                    epsabs=tolerance, args=(snr, 4))
    Pe_8[i], error = integrate.quad(bdt_int2, 0, plus_inf,
                                    epsabs=tolerance, args=(snr, 8))

    Pe_16[i], error = integrate.quad(bdt_int2, 0, plus_inf,
                                     epsabs=tolerance, args=(snr, 16))

    Pe_32[i], error = integrate.quad(bdt_int2, 0, plus_inf,
                                     epsabs=tolerance, args=(snr, 32))

Pe_2 = 1 - np.array(Pe_2)
Pe_4 = 1 - np.array(Pe_4)
Pe_8 = 1 - np.array(Pe_8)
Pe_16 = 1 - np.array(Pe_16)
Pe_32 = 1 - np.array(Pe_32)

#     选择一：直接打印

print("Pe_2：", Pe_2)
print("Pe_4：", Pe_4)
print("Pe_8：", Pe_8)
print("Pe_16：", Pe_16)
print("Pe_32：", Pe_32)


#     选择二：写入到当前目录的result.txt文件
# fmt元素类型 、 delimiter间隔符
# np.savetxt(".\Pe_2.csv", Pe_2, fmt='%f', delimiter=',')
# np.savetxt(".\Pe_4.txt", Pe_4, fmt='%f', delimiter=',')
# np.savetxt(".\Pe_8.txt", Pe_8, fmt='%f', delimiter=',')
# np.savetxt(".\Pe_16.txt", Pe_16, fmt='%f', delimiter=',')
# np.savetxt(".\Pe_32.txt", Pe_32, fmt='%f', delimiter=',')
# np.savetxt(".\Pe_64.txt", Pe_64, fmt='%f', delimiter=',')
