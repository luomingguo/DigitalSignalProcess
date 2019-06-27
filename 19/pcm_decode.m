function [out]= pcm_decode(in,v)
%decode the input pcm code 
%in :   input the pcm code 8bit/sample
%v:     quantized level
n=length(in);
 
in = reshape(in',8,n/8)';
slot(1) = 0;
slot(2) = 32;
slot(3) = 64;
slot(4) = 128;
slot(5) = 256;
slot(6) = 512;
slot(7) = 1024;
slot(8) = 2048;
 
step(1) = 2;
step(2) = 2;
step(3) = 4;
step(4) = 8;
step(5) = 16;
step(6) = 32;
step(7) = 64;
step(8) = 128;
 
 
for i=1:n/8
   ss = 2*in(i,1)-1;
   tmp= in(i,2)*4+in(i,3)*2+in(i,4)+1;
   st = slot(tmp);
   dt = (in(i,5)*8+in(i,6)*4+in(i,7)*2+in(i,8))*step(tmp) + 0.5*step(tmp);
   out(i)=ss*(st+dt)/4096*v;
end
