
import numpy as np
def entropy(p):
    # if length(find(p < 0))~=0,
    # error('Not a prob. vector, negative component(s)')
    if sum(p < 0) != 0:
        return

    if abs(sum(p) - 1) > 10e-10:
        return

    return sum(-p * np.log2(p))