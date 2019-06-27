import numpy as np
def nextpow2(x):
    return int(round(np.log(x)/np.log(2)))