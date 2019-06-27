import numpy as np

import matplotlib.pyplot as plt
def function2():
    c = np.zeros((45, 51))
    w=np.hstack((np.arange(1, 20.5, 5),np.arange(25,100.5,20),np.arange(130, 300.5, 50),\
      np.arange(400,1001,100),np.arange(1250,5001,250),np.arange(5500,10001,500)))

    pn0_db=np.arange(-20,31)
    pn0 = 10 ** (pn0_db/10)
    for i in range(45):
      for j in range(51):
        c[i,j]=w[i]*np.log2(1+pn0[j]/w[i])

    k=[0.9,0.8,0.5,0.6];
    s=[-70,35]

    # python 包不含由类似surfl类型的模块或方法

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(w, pn0_db, title='Capacity vs. bandwidth and SNR')
    # surfl(w,pn0_db,c',s,k)
    # title('Capacity vs. bandwidth and SNR')

if __name__ == '__main__':
    function2()