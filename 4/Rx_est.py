import numpy as np


def Rx_est(X, M):

    N = len(X)
    Rx = np.zeros((1,M+1), dtype=float)
    for m in range(M+1):
        for n in range(N-m+1):
            Rx[0][m] += X[n-1] * X[n+m-1]


        Rx[0][m] /= N-m+1
    return Rx

# function [Rx]=Rx_est(X,M)
# N=length(X);
# Rx=zeros(1,M+1);
# for m=1:M+1,
#   for n=1:N-m+1,
#     Rx(m)=Rx(m)+X(n)*X(n+m-1);
#   end;
#   Rx(m)=Rx(m)/(N-m+1);
# end;

