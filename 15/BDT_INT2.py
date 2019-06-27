import numpy as np
from  q import q

def bdt_int2(x,snr_per_bit,M):
    E=1
    Eb=E/np.log2(M)
    sgma=Eb*np.sqrt(np.log2(M)/(2*snr_per_bit))

    return (1-2*q(x/sgma)) ** (M/2-1)*(1/(np.sqrt(2*np.pi)*sgma))*np.exp(-(x-E)**2/(2*sgma**2))
