import numpy as np
import matplotlib.pyplot as plt

def _correlation(x, h):
    len_x = len(x)
    len_h = len(h)
    output_length = len_x + len_h - 1
    y = np.zeros(output_length)
    
    for k in range(output_length):
        y_k = 0
        for n in range(len_x):
            if 0 <= n - k + len_h - 1 < len_h:
                y_k += x[n] * h[n - k + len_h - 1]
        y[k] = y_k

    return y

# Input sequences
x = [0, 1, 2, 3]
h = x

# Compute cross-correlation
cross_correlation = _correlation(x, h)
correlate = np.correlate(x, h, mode='full')
print("Cross-correlation result:", cross_correlation)
print("Cross correlation using numpy:", correlate)