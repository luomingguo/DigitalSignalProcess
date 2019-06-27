import numpy as np

def gngauss(m=0,sgma=1):
    u = np.random.rand()
    z = sgma * (np.sqrt(2 * np.log(1 / (1 - u))))
    u = np.random.rand()
    gsrv1 = m + z * np.cos(2 * np.pi * u)
    gsrv2 = m + z * np.sin(2 * np.pi * u)
    return gsrv1, gsrv2