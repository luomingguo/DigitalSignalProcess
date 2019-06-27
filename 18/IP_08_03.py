import numpy as np
from scipy.integrate import quad
from il3_8fun import il3_8fun
import matplotlib.pyplot as plt
a_db = np.arange(-20, 20.1, 0.2)
a = 10 ** (a_db / 10)
c= np.zeros(201)
tolerance = 1e-3
for i in range(201):

  f ,err=quad(il3_8fun,a[i]-5,a[i]+5,epsabs=tolerance,args=(a[i]))
  g ,err=quad(il3_8fun,-a[i]-5,-a[i]+5,epsabs=tolerance,args=(-a[i]))
  c[i]=0.5 * f + 0.5 * g

fig = plt.figure(1, figsize=(13, 8), dpi=98)
fig.add_subplot(111, title="Capacity versus SNR in binary input AWGN channel", xlabel='SNR', ylabel="Capacity (bits/transmission)")
plt.semilogx(a,c)
plt.show()