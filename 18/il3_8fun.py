import numpy as np

def il3_8fun(x,*args):
    return 1 / np.sqrt(2 * np.pi) * np.exp((-(x - args[0]) ** 2) / 2) * np.log2(2 / (1 + np.exp(-2 * x * args[0])))

    # function f=il3_8fun(x,args[0])
    # f=1/sqrt(2*pi)*exp((-(x-args[0]).^2)/2).*log2(2./(1+exp(-2*x.*args[0])));