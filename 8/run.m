echo on
n=[-20:1:20];
x=.5*(sinc(n/2)).^2;
figure(1);
plot(n,x);
ylim([0,0.6]);
figure(2);
stem(n,x)
ylim([0,0.6]);
ts=1/40;
t=[-0.5:ts:1.5];
fs=1/ts;
b=[zeros(1,20),t(21:61),zeros(1,20)];
H=fft(b)/fs;
df=fs/80;
f=[0:df:fs]-fs/2;
H1=fftshift(H);
y=x.*H1(21:61);
figure(3);
stem(n,y);
ylim([-0.2,0.3]);