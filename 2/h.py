from scipy.stats import entropy
import numpy as np
def entropy2(p):

    return entropy(np.array([p, 1-p]))
