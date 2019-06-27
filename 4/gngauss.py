
import numpy as np

def gngauss(m=0, sgma=1):


    u1 = np.random.random()
    u2 = np.random.random()
    z = sgma * (np.sqrt(2  * np.log(1 / (1 - u1))))
    gsrv1 = m + z * np.cos(2 * np.pi * u2)
    gsrv2 = m + z * np.sin(2 * np.pi * u2)

    return gsrv1, gsrv2

# function [gsrv1,gsrv2] =gngauss(m,sgma)
# if nargin ==0,
#     m=0; sgma=1;
# elseif nargin == 1,
#     sgma=m; m=0;
# end
# u=rand;
# z=sgma*(sqrt(2*log(1/(1-u))));
# u=rand;
# gsrv1=m+z*cos(2*pi*u);
# gsrv2=m+z*sin(2*pi*u);
# end

#