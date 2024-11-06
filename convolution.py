import numpy as np
import matplotlib.pyplot as plt

def _convolution(x , h):
    result_length = len(x) + len(h) - 1
    yn = np.zeros(result_length)

    for n in range(result_length):
        y_n = 0
        for k in range(len(x)):
            if 0 <= n-k < len(h):
                y_n += x[k] * h[n-k]
        yn[n] = y_n
    
    return yn

#main

x = list(map(int , input("Enter elements of x: ").split()))
h = list(map(int , input("Enter the values fo h: ").split()))

convolution = _convolution(x,h)
print(convolution)

convolution = np.convolve(x,h)
print(convolution)