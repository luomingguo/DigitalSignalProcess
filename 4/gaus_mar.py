import numpy as np
from gngauss import gngauss


def gaus_mar(X0, rho, N):

    Ws = np.arange(N, dtype=float)
    X  = np.arange(N, dtype=float)
    for i in range(0, N, 2):
        Ws[i], Ws[i+1] = gngauss()

    X[0] = rho * X0 + Ws[0]
    for i in range(1, N):
        X[i] = rho * X[i-1] + Ws[i]
    print(X)
    return X


# function [X]=gaus_mar(XO,rho,N)
# for i=1:2:N,
#      [Ws(i) Ws(i+1)]=gngauss;
#     end;
#     X(1)=rho*XO+Ws(1);
#     for i=2:N,
#       X(i)=rho*X(i-1)+Ws(i);
# end
