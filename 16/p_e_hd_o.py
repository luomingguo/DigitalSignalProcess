import numpy as np
from q import q

def p_e_hd_o(gamma_db_l,gamma_db_h,k,n,d_min):
    gamma_db = np.arange(gamma_db_l, gamma_db_h + (gamma_db_h - gamma_db_l) / 40, (gamma_db_h - gamma_db_l) / 20)
    gamma_b = 10 ** (gamma_db / 10)
    R_c = k / n
    p_b = q(np.sqrt(R_c * gamma_b))
    p_err = (2 ** k - 1) * (4 * p_b * (1 - p_b)) ** (d_min / 2)
    return  p_err, gamma_db
