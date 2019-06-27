function [X]=gaus_mar(XO,rho,N)
for i=1:2:N,
     [Ws(i) Ws(i+1)]=gngauss;
    end;
    X(1)=rho*XO+Ws(1);
    for i=2:N,
      X(i)=rho*X(i-1)+Ws(i);
end

