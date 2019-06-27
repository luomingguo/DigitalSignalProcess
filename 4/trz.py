from matplotlib import pyplot as plt
import numpy as np
from gaus_mar import gaus_mar
from Rx_est import Rx_est

rho = 0.95
X0 = 0
N = 1000
X = gaus_mar(X0, rho, N)
M = 50
Rx = Rx_est(X,M)
fig = plt.figure(21, figsize=(13, 8), dpi=98)

fig.add_subplot(211)
plt.plot(X)
plt.grid()

fig.add_subplot(212)
K2 = np.arange(0,51)
plt.plot(K2, Rx[0])

plt.grid()
plt.show()


# echo on;
# rho=0.95;
# XO=0;
# N=1000;
# X=gaus_mar(XO,rho,N);
# M=50;
# Rx=Rx_est(X,M);
# figure(1);
# plot(X);
# figure(2);
# plot(Rx);