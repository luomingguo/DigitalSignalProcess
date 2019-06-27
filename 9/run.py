import numpy as np

import matplotlib.pyplot as plt
def run():
    ep = 0.3
    p = np.zeros(62)
    print(p.shape)
    for i in range(0,61, 2):
        p[i]=0
        # for j=(i+1)/2:i
        for j in range(i // 2, i):
            p[i] += np.prod(np.arange(1,i+0.1)) / (np.prod(np.arange(1,j+0.1)) * np.prod(np.arange(1,(i-j+0.1)))) \
            * ep ** j * (1-ep) ** (i-j)


    fig = plt.figure(1, figsize=(13,7), dpi=98)
    fig.add_subplot(111, xlabel="n", ylabel="pe")
    plt.stem(np.arange(0, 60, 2), p[0:60:2])
    plt.grid("-.")
    plt.show()

if __name__ == '__main__':
    run()