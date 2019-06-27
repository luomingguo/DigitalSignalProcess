echo on;
rho=0.95;
XO=0;
N=1000;
X=gaus_mar(XO,rho,N);
M=50;
Rx=Rx_est(X,M);
figure(1);
plot(X);
figure(2);
plot(Rx);




