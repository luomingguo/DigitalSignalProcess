import numpy as np

import matplotlib.pyplot as plt
from SMLDPE55 import SMLDPE55
from q import   q

SNRindB1 = np.arange(0,11,1)
SNRindB2= np.arange(0,11.1,0.1)
smld_err_prb = np.zeros(len(SNRindB1))
theo_err_prb = np.zeros(len(SNRindB2))
for i in range(len(SNRindB1)):
    smld_err_prb[i]=SMLDPE55(SNRindB1[i])

for i in range(len(SNRindB2)):
    SNR=np.exp(SNRindB2[i]*np.log(10)/10)

    theo_err_prb[i]=q(np.sqrt(2*SNR))

plt.semilogy(SNRindB1,smld_err_prb,'*')
plt.semilogy(SNRindB2,theo_err_prb)
plt.show()