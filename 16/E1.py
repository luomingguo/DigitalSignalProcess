from p_e_hd_a import p_e_hd_a
from p_e_hd_o import p_e_hd_o
from p_e_sd_o import p_e_sd_o
from p_e_sd_a import p_e_sd_a
import matplotlib.pyplot as plt
(p_err_ha,gamma_b_1)=p_e_hd_a(10,16,11,15,3)
(p_err_ho,gamma_b_2)=p_e_hd_o(10,16,11,15,3)
(p_err_so,gamma_b_3)=p_e_sd_o(7,13,11,15,3)
(p_err_sa,gamma_b_4)=p_e_sd_a(7,13,11,15,3)
fig = plt.figure(1, (13,8), 98)
plt.subplot(111)
plt.semilogy(gamma_b_1,p_err_sa,'-.',gamma_b_2,p_err_so,'-*', gamma_b_3,p_err_ha,'-.',gamma_b_4,p_err_ho,'-*')
plt.grid()
# plt.semilogy(gamma_b_1,p_err_sa,'-.')
plt.show()