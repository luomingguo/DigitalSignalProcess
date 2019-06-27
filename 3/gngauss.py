import numpy as np
def gngauss(mean,sgma):

    u=np.random.uniform()                         	# a uniform random variable in (0,1)
    z=sgma*(np.sqrt(2*np.log(1/(1-u))))  # a Rayleigh distributed random variable
    u=np.random.uniform()                         	# another uniform random variable in (0,1)
    return (mean + z * np.sin(2 * np.pi*u))