import numpy as np
import matplotlib.pyplot as plt

def _convolution(x , h):
    result_length = len(x) + len(h) - 1
    
    y = np.zeros(result_length)

    for n in range (result_length):
        y_n = 0
        for k in range(len(x)):
            if 0 <= n-k < len(h):
                y_n += x[k] * h[n-k]
        y[n] = y_n
    return y


#define parameters
x = [1,2,1,-1]
h = [1,2,3,1]

convolution = _convolution(x,h)
conovol = np.convolve(x,h)

print(convolution)
print(conovol)