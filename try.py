import numpy as np
import matplotlib.pyplot as plt

def _correlation(x,h):
    result_length = len(x) + len(h) - 1
    yk = np.zeros(result_length)

    for n in range(result_length):
        y_k = 0
        for k in range(len(x)):
            if 0 <= n-k < len(h):
                y_k += x[k] * h[n-k]
        
        yk[n] = y_k
    
    return yk

#main
x = list(map(int , input("Enter the values of x: ").split()))
h = list(map(int , input("Enter the values of h: ").split()))

correlation = np.correlate(x,h, mode='full')
print(correlation)

h.reverse()
correlation = _correlation(x,h)
print(correlation)

