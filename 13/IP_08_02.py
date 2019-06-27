import numpy as np
import matplotlib.pyplot as plt


pn0_db = np.arange(-20,30.001,0.1)

pn0=10 ** (pn0_db / 10)

capacity=3000 * np.log2(1 + pn0 / 3000)

fig = plt.figure(1, (15,8), dpi=98)
plt.subplot(211, title='Capacity vs. P/N0 in an AWGN channel', xlabel='P/N0',ylabel='Capacity (bits/second)')
plt.semilogx(pn0,capacity)

w= np.hstack((np.arange(1,10),np.arange(12,101,2),np.arange(105,501,5),np.arange(510,5001,10),np.arange(5025,20001,25), \
             np.arange(20050,100001,50)))
pn0_db=25
pn0=10 ** (pn0_db/10)
capacity=w * np.log2(1+pn0 / w)
plt.subplot(111, title='Capacity vs. bandwidth in an AWGN channel', xlabel='Bandwidth (Hz)',ylabel='Capacity (bits/second)')
plt.semilogx(w,capacity)
plt.grid()
plt.show()
