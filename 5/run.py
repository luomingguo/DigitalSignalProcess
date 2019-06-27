import  numpy as np
import matplotlib.pyplot as plt
from fftseq import  fftseq
df=0.01
fs=10
ts=1/fs
t = np.arange(-5, 5,ts)
x1=np.zeros(len(t))
x1[40:50] += 1
x1[51:60]= 0
x2=np.zeros(len(t))
for i in range(21):
    x2[i+50]=x1[40+i]
X1,x11,df1=fftseq(x1,ts,df)
X2,x21,df2=fftseq(x2,ts,df)
X11=X1/fs
X21=X2/fs
f=np.arange(0, len(x11) * df1, df1) - fs/2
plt.plot(f, np.fft.fftshift(abs(X11)))

plt.plot(f[500:525],np.fft.fftshift(np.angle(X11[500:525])),'r^',f[500:525],np.fft.fftshift(np.angle(X21[500:525])),'-*')
plt.show()