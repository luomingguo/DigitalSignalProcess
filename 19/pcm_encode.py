import numpy as np
from dec2bin import dec2bin


def pcm_encode(x):

    x = np.zeros(n)  # 1001*8
    for i in range(n):

        if x> 0:
            out[i][0] = 1
        else:
            out[i][0] = 0

        if np.abs(x[i]) >= 0 and np.abs(x[i]) < 32:

            out[i][1] = 0
            out[i][2] = 0
            out[i][3] = 0
            step = 2
            st = 0

        elif 32 <= np.abs(x[i]) and np.abs(x[i]) < 64:
            out[i][1] = 0
            out[i][2] = 0
            out[i][3] = 1
            step = 2
            st = 32
        elif 64 <= np.abs(x[i]) and np.abs(x[i]) < 128:
            out[i][1] = 0
            out[i][2] = 1
            out[i][3] = 0
            step = 4
            st = 64
        elif 128 <= np.abs(x[i]) and np.abs(x[i]) < 256:
            out[i][1] = 0
            out[i][2] = 1
            out[i][3] = 1
            step = 8
            st = 128
        elif 256 <= np.abs(x[i]) and np.abs(x[i]) < 512:
            out[i][1] = 1
            out[i][2] = 0
            out[i][3] = 0
            step = 16
            st = 256
        elif 512 <= np.abs(x[i]) and np.abs(x[i]) < 1024:
            out[i][3] = 1
            out[i][3] = 0
            out[i][3] = 1
            step = 32
            st = 512
        elif 1024 <= np.abs(x[i]) and np.abs(x[i]) < 2048:
            out[i][1] = 1
            out[i][2] = 1
            out[i][3] = 0
            step = 64
            st = 1024
        elif 2048 <= np.abs(x[i]) and np.abs(x[i]) < 4096:
            out[i][1] = 1
            out[i][2] = 1
            out[i][3] = 1
            step = 128
            st = 2048
        else:
            out[i][1] = 1
            out[i][2] = 1
            out[i][3] = 1
            step = 128
            st = 2048

        if (np.abs(x[i]) >= 4096):
            out[i, 1: 7] = np.array([1, 1, 1, 1, 1, 1, 1])
        else:
            tmp = np.floor((np.abs(x[i]) - st) / step)
            bin_temp = dec2bin(tmp)
            while len(bin_temp) < 5:
                bin_temp = '0' + bin_temp
            t = np.zeros(4)
            for i in range(4):
                t[i] = int(bin_temp[i]) - int(chr(48))
            print()
            out[i, 4: 7] = t[:3]

    out = out.reshape(1, 8 * n, order='f')
    return out

# def pcm_encode(x):
#
#
#     n = len(x) #1001
#     out = np.zeros((n,8))
#     x = np.zeros(n) # 1001*8
#     for i in range(n):
#
#         if x[i] > 0:
#             out[i][0] = 1
#         else:
#             out[i][0] = 0
#
#         if np.abs(x[i]) >= 0 and np.abs(x[i]) < 32:
#
#             out[i][1] = 0
#             out[i][2] = 0
#             out[i][3] = 0
#             step = 2
#             st = 0
#
#         elif  32 <= np.abs(x[i]) and np.abs(x[i]) < 64:
#             out[i][1] = 0
#             out[i][2] = 0
#             out[i][3] = 1
#             step = 2
#             st = 32
#         elif 64 <= np.abs(x[i]) and np.abs(x[i]) < 128:
#             out[i][1] = 0
#             out[i][2] = 1
#             out[i][3] = 0
#             step = 4
#             st = 64
#         elif 128 <= np.abs(x[i]) and np.abs(x[i]) < 256:
#             out[i][1] = 0
#             out[i][2] = 1
#             out[i][3] = 1
#             step = 8
#             st = 128
#         elif 256 <= np.abs(x[i]) and np.abs(x[i]) < 512:
#             out[i][1] = 1
#             out[i][2] = 0
#             out[i][3] = 0
#             step = 16
#             st = 256
#         elif 512 <= np.abs(x[i]) and np.abs(x[i]) < 1024:
#             out[i][3] = 1
#             out[i][3] = 0
#             out[i][3] = 1
#             step = 32
#             st = 512
#         elif 1024 <= np.abs(x[i]) and np.abs(x[i]) < 2048:
#             out[i][1] = 1
#             out[i][2] = 1
#             out[i][3] = 0
#             step = 64
#             st = 1024
#         elif 2048 <= np.abs(x[i]) and np.abs(x[i]) < 4096:
#             out[i][1] = 1
#             out[i][2] = 1
#             out[i][3] = 1
#             step = 128
#             st = 2048
#         else:
#             out[i][1] = 1
#             out[i][2] = 1
#             out[i][3] = 1
#             step = 128
#             st = 2048
#
#         if (np.abs(x[i]) >= 4096):
#             out[i, 1: 7] = np.array([1,1,1,1,1,1,1])
#         else:
#             tmp = np.floor((np.abs(x[i]) - st) / step)
#             bin_temp = dec2bin(tmp)
#             while len(bin_temp)< 5:
#                 bin_temp = '0' + bin_temp
#             t = np.zeros(4)
#             for i in range(4):
#                 t[i] = int(bin_temp[i]) - int(chr(48))
#             print()
#             out[i, 4: 7] =t[:3]
#
#     out = out.reshape(1,8*n, order='f')
#     return out