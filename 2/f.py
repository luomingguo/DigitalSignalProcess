import math
def il3_8fun(x,p):
    return 1 / math.sqrt(2 * math.pi) * math.exp((-(x - p) ** 2) * math.log(2 / (1 + math.exp(-2 * x * p)), 2))