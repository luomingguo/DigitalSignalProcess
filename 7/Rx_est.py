import numpy as np

def Rx_est(X,M):

    N = len(X[0])
    Rx = np.zeros((1, M + 1)) # 1*51
    for m in range(M):
    # for m=1:M + 1,
    #     for n=1:N - m + 1,
        for n in range(N-m):
            Rx[0][m] += X[0][n] * X[0][n + m - 1]
            Rx[0][m] /= N - m + 1
    return Rx