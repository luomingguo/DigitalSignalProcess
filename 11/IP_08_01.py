import numpy as np
from  q  import q
from entropy2 import entropy2
import matplotlib.pyplot as plt
# gamma_db=[-20:0.1:20];
gamma_db = np.arange(-20, 20+0.01, 0.1)  # (401,)

# gamma=10.^(gamma_db./10);
gamma = 10 ** (gamma_db / 10)  # (401,)

# p_error=q(sqrt(2.*gamma));
p_error =q(np.sqrt(2 * gamma))

capacity=1 - entropy2(p_error)

fig = plt.figure(21, figsize=(13, 8), dpi=98)

fig.add_subplot(211, xlabel='SNR/bit', ylabel='Error Prob.', title='Error probability versus SNR/bit')
plt.semilogx(gamma,p_error)
plt.grid()

fig.add_subplot(212, xlabel='SNR/bit', ylabel='Channel capacity', title='Channel capacity versus SNR/bit')
plt.semilogx(gamma,capacity)
plt.grid()
plt.subplots_adjust(wspace=1, hspace=1)
fig.tight_layout()
plt.show()

# semilogx(gamma,p_error)
# xlabel('SNR/bit')
# title('Error probability versus SNR/bit')
# ylabel('Error Prob.')
# pause % Press a key to see a plot of channel capacity vs. SNR/bit
# clf
# semilogx(gamma,capacity)
# xlabel('SNR/bit')
# title('Channel capacity versus SNR/bit')
# ylabel('Channel capacity')
