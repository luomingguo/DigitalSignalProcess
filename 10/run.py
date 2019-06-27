import numpy as np
import matplotlib.pyplot as plt


n=5
m = np.arange(0, -3+(-0.5 * 0.1), -0.5)

pe = 10 ** m

d=(np.sign(np.random.randn(1,100000))+1) / 2
# print(d.shape) # 1,10000
s= np.row_stack((d,d, d, d,d))
# print(s.shape) # 5,10000
s=s.reshape((1,-1))
error = np.zeros(m.shape[0])

for  k in range(m.shape[0]):
    err=np.random.rand(1,d.shape[1]*5)
    err = (err < pe[k]) + 0
    r=(s+err) % 2
    r = r.reshape((5,d.shape[1]))
    dd = (sum(r)>2) + 0
    error[k] = sum(abs(dd-d[0]))/len(d[0])

plt.loglog(pe,error)
plt.show()

#n=5;
# m=0:-0.5:-3;
# pe=10.^m;
#
# d=(sign(randn(1,100000))+1)/2;
# s=[d;d;d;d;d];
# s=reshape(s,1,5*length(d));
# for k=1:length(pe)
# err=rand(1,length(d)*5);
# err=err<pe(k);
# r=rem(s+err,2);
# r=reshape(r,5,length(d));
# dd=sum(r)>2;
# error(k)=sum(abs(dd-d))/length(d);
# end
# loglog(pe,error)