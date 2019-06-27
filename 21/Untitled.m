%QPSK & OQPSK
clear all;
close all;
 
M = 4;
Ts= 1;
fc= 10;
N_sample = 16;
N_num = 100;
 
dt = 1/fc/N_sample;
t = 0:dt:N_num*Ts-dt;
T = dt*length(t);
 
py1f = zeros(1,length(t));    %功率谱密度1
py2f = zeros(1,length(t));    %功率谱密度2
 
for PL=1:100   %输入100段N_num个码字的波形，为了使功率谱密度看起来更加平滑，
               %可以取这100段信号功率谱密度的平均
    d1 = sign(randn(1,N_num));
    d2 = sign(randn(1,N_num));
    gt = ones(1,fc*N_sample);
 
    %QPSK调制
    s1 = sigexpand(d1,fc*N_sample);
    s2 = sigexpand(d2,fc*N_sample);
    b1 = conv(s1,gt);
    b2 = conv(s2,gt);
    s1 = b1(1:length(s1));
    s2 = b2(1:length(s2));
 
    st_qpsk = s1.*cos(2*pi*fc*t) - s2.*sin(2*pi*fc*t);
 
    s2_delay= [-ones(1,N_sample*fc/2) s2(1:end-N_sample*fc/2)];
    st_oqpsk= s1.*cos(2*pi*fc*t) - s2_delay.*sin(2*pi*fc*t);
 
    %经过带通后，再经过非线性电路
    [f y1f] = T2F(t,st_qpsk);
    [f y2f] = T2F(t,st_oqpsk);
    [t y1] = bpf(f,y1f,fc-1/Ts,fc+1/Ts);
    [t y2] = bpf(f,y2f,fc-1/Ts,fc+1/Ts);
    subplot(221);
    plot(t,y1); xlabel('t');ylabel('QPSK波形');
    axis([5 15 -1.6 1.6]);title('经过带通后的波形');
 
    subplot(222)
    plot(t,y2);  xlabel('t'); ylabel('OQPSK波形');
    axis([5 15 -1.6 1.6]);title('经过带通后的波形');
 
    %经过非线性电路
    y1 = 1.5*tanh(2*y1);
    y2 = 1.5*tanh(2*y2);
    [f y1f] = T2F(t,y1);
    [f y2f] = T2F(t,y2);
    py1f = py1f + abs(y1f).^2/T;     %QPSK不同段信号功率谱密度相加
    py2f = py2f + abs(y2f).^2/T;     %OQPSK不同段信号功率谱密度相加
end
py1f = py1f/100;                     %QPSK 100段功率谱密度平均
py2f=py2f/100;                       %OQPSK 100段功率谱密度平均
   
subplot(223);
plot(f,10*log10(py1f)); xlabel('f');ylabel('QPSK功率谱密度(dB/Hz)');
title('经过非线性电路后的功率谱密度');axis([ -15 15 -30 10]);
 
subplot(224)
plot(f,10*log10(py2f));xlabel('f');ylabel('OQPSK功率谱密度(dB/Hz)');
title('经过非线性电路后的功率谱密度');axis([ -15 15 -30 10]);
 
figure(2)
x = -2:0.1:2;
y=1.5*tanh(2*x);
plot(x,y); title('非线性电路的输入输出函数');
