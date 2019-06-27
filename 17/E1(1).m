% MATLAB script for Illustrative Problem 8, Chapter 6.
echo on
N=31;
T=1;
W=1/(2*T);
n=-(N-1)/2:(N-1)/2;			% The indeces for g_T
% The expression for g_T is obtained next
for i=1:length(n),
  g_T(i)=0;
  for m=-(N-1)/2:(N-1)/2,
    if ( abs((4*m)/(N*T)) <= W ),
      g_T(i)=g_T(i)+sqrt((1/W)*cos((2*pi*m)/(N*T*W)))*exp(j*2*pi*m*n(i)/N);
    end;
  end;
end;
% obtain g_T(n-(N-1)/2)
figure(1);
stem(n,g_T)
n2=0:N-1;
% obtain the frequency response characteristics
[G_T,W]=freqz(g_T,1);
% normalized magnitide response  
magG_T_in_dB=20*log10(abs(G_T)/max(abs(G_T)));
figure(2);
plot(W,magG_T_in_dB)
% Impulse response of the cascade of the transmitter and the receiver filters..
g_R=g_T;
imp_resp_of_cascade=conv(g_R,g_T);
figure(3);
stem(imp_resp_of_cascade);
% plotting commands follow