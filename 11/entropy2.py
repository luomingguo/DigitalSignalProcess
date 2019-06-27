import numpy as np
from entropy import entropy
def entropy2(p):
    n = len(p)
    h = np.zeros(n)

    for i in range(n):
        p1 = np.hstack((p[i], 1-p[i]))
        h[i] = entropy(p1)
    return h

    # n=length(p);
    # for i=1:n
    # p1=[p(i) 1-p(i)];
    # h(i)=entropy(p1);
    # end