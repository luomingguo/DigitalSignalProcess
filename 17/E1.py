import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, convolve
N=31
T=1
W=1/(2*T)
# n=-(N-1)/2:(N-1)/2
n = np.arange(-(N-1) / 2 , (N-1)/ 2 + 0.5, 1)

g_T = np.zeros(len(n), dtype=complex)
j = round(0,1)
for i in range(len(n)):
    g_T[i]=0
    for m in range(-(N-1)//2,(N-1)//2+1):
        if ( abs((4*m)/(N*T)) <= W ):
            g_T[i] += np.sqrt((1/W) * np.cos((2 * np.pi * m)/(N * T * W))) * np.exp(j * 2 * np.pi * m * n[i]/N)

fig = plt.figure(1, (15,8), dpi=98)
plt.subplot(221)
plt.stem(n,g_T)

# n2=0:N-1
n2 = np.arange(0,N)

# [G_T,W]=freqz(g_T,1)
G_T, W = freqz(g_T, 1)
magG_T_in_dB=20*np.log10(abs(G_T)/max(abs(G_T)));
plt.subplot(222)
plt.plot(W, magG_T_in_dB)

g_R=g_T
imp_resp_of_cascade=convolve(g_R,g_T)
plt.subplot(223)
plt.stem(imp_resp_of_cascade)
plt.show()