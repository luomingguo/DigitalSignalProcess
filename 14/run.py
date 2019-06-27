import  numpy as np
import  matplotlib.pyplot as plt
dx =0.01
x= np.arange(-1,1+0.1*dx, dx)

u = 255
A = 87.6

yu = np.sign(x) * np.log(1 + u * abs(x)) / np.log(1 + u)
ya = np.zeros(len(x))
for i in range(len(x)):

    if abs(x[i]) < 1 / A:
        ya[i] = A * x[i] / (1 + np.log(A))
    else:
        ya[i] = np.sign(x[i]) * (1 + np.log(A * abs(x[i]))) / (1 + np.log(A))


fig = plt.figure(1, (15,8), dpi=98)
plt.subplot(211, title='u Law', xlabel='x',ylabel='y')
plt.plot(x, yu, 'k.:')
plt.grid("-*")

xx = [-1, -127 / 255, -63 / 255, -31 / 255, -15 / 255, -7 / 255, -3 / 255, -1 / 255, 1 / 255, 3 / 255, 7 / 255,
      15 / 255, 31 / 255, 63 / 255,127 / 255, 1]
yy = [-1, -7 / 8, -6 / 8, -5 / 8, -4 / 8, -3 / 8, -2 / 8, -1 / 8, 1 / 8, 2 / 8, 3 / 8, 4 / 8, 5 / 8, 6 / 8, 7 / 8, 1]
plt.plot(xx, yy, 'r')
plt.stem(xx, yy, 'b-.')
plt.legend((xx, yy),('u律压缩特性', '折线近似u律'), loc='lower left')

plt.subplot(212, title='A Law', xlabel='x',ylabel='y')
plt.plot(x, ya, 'k.:')
plt.grid('-.')

xx = [-1, -1 / 2, -1 / 4, -1 / 8, -1 / 16, -1 / 32, -1 / 64, -1 / 128, 1 / 128, 1 / 64, 1 / 32, 1 / 16, 1 / 8, 1 / 4,
      1 / 2, 1]
yy = [-1, -7 / 8, -6 / 8, -5 / 8, -4 / 8, -3 / 8, -2 / 8, -1 / 8, 1 / 8, 2 / 8, 3 / 8, 4 / 8, 5 / 8, 6 / 8, 7 / 8, 1]
plt.plot(xx, yy, 'r')
plt.stem(xx, yy, 'b-.')
plt.legend((xx, yy),('A律压缩特性', '折线近似A律'), loc='lower left')
plt.show()