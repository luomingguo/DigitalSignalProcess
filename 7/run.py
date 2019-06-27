import numpy as np
from Rx_est import Rx_est

def run():
    N=1000 #最大值
    M=50
    Rxav=np.zeros((1,M+1))
    Ryav=np.zeros((1,M+1))
    Sxav=np.zeros((1,M+1))
    Syav=np.zeros((1,M+1))
    Y = np.zeros((1,N))
    for i in range(10):
        # for i=1:10

        X = np.random.rand(1,N)-1/2			# Generate a uniform number sequence on (-1/2,1/2)
        Y[0][1]=0
        # for n=2:N,
        for n in range(1,N):
            Y[0][n] = 0.9*Y[0][n-1] + X[0][n]         # note that Y(n) means Y(n-1)

        print("X",X.shape)

        Rx=Rx_est(X,M)		# Autocorrelation of {Xn}
        print("Rx",Rx.shape)
        Ry=Rx_est(Y,M)		# Autocorrelation of {Yn}
        Sx=np.fft.fftshift(abs(np.fft.fft(Rx[0])))	        # Power spectrum of {Xn}
        Sy=np.fft.fftshift(abs(np.fft.fft(Ry[0])))	        # Power spectrum of {Yn}

        Rxav=Rxav+Rx
        Ryav=Ryav+Ry
        Sxav=Sxav+Sx
        Syav=Syav+Sy

    Rxav /= 10
    Ryav /= 10
    Sxav /= 10
    Syav /= 10

if __name__ == '__main__':
    run()