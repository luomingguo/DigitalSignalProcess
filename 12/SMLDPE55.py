
import numpy as np
from gngauss import  gngauss
def SMLDPE55(snr_in_dB):
    E = 1
    SNR = np.exp(snr_in_dB * np.log(10) / 10)
    sgma = E / np.sqrt(2 * SNR)
    N = 10000
    dsource = np.zeros(N)
    for i in range(N):
        temp = np.random.rand()
        if (temp < 0.5):
            dsource[i] = 0
        else:
            dsource[i]=1
    numoferr=0
    for i in range(N):
       if (dsource[i]==0):
          r = -E + sum(gngauss(sgma=sgma))
       else:
          r=E+sum(gngauss(sgma=sgma))
       if (r<0):
          decis=0		 
       else:
          decis=1
       if (decis!=dsource[i]):    	
          numoferr=numoferr+1
  
    p=numoferr/N
    return p