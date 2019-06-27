% MATLAB script for Illustrative Problem 9, Chapter 2.
N=1000;	               			% The maximum value of n
M=50;
Rxav=zeros(1,M+1);
Ryav=zeros(1,M+1);
Sxav=zeros(1,M+1);
Syav=zeros(1,M+1);
for i=1:10,	       			% take the ensemble average ove 10 realizations
   X=rand(1,N)-(1/2);  			% Generate a uniform number sequence on (-1/2,1/2)
   Y(1)=0;
   for n=2:N,
      Y(n) = 0.9*Y(n-1) + X(n);         % note that Y(n) means Y(n-1)
   end;
   Rx=Rx_est(X,M);			% Autocorrelation of {Xn}
   Ry=Rx_est(Y,M);			% Autocorrelation of {Yn}
   Sx=fftshift(abs(fft(Rx)));	        % Power spectrum of {Xn}
   Sy=fftshift(abs(fft(Ry)));	        % Power spectrum of {Yn}
   Rxav=Rxav+Rx;
   Ryav=Ryav+Ry;
   Sxav=Sxav+Sx;
   Syav=Syav+Sy; 
end;
Rxav=Rxav/10;
Ryav=Ryav/10;
Sxav=Sxav/10;
Syav=Syav/10;
% Plotting commands follow