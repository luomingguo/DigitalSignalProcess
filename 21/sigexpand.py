import numpy as np

def sigexpand(d, M):
    temp_array = np.zeros([M, len(d)])

    temp_array[0] = d

    # print("temp_array", temp_array.shape)
    return temp_array.reshape((1, -1), order='F')


# function[out]=sigexpand(d,M)
# N=length(d);
# out=zeros(M,N);
# out(1,:)=d;
# out=reshape(out,1,M*N);