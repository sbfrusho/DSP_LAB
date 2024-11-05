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
# x = [1,2,3,4,5]
# h = [1,2,3,4]

x = list(map(int, input("Enter elements for x: ").split()))

h = list(map(int, input("Enter elements for h:").split()))

convolution = _convolution(x,h)
conovol = np.convolve(x,h)

k = np.arange(len(x) + len(h) - 1)

print(convolution)
print(conovol)

# plt.figure(figsize=(12,8))

# plt.subplot(3,2,1)
# plt.stem(k , convolution)
# plt.title("Correlation of x and h")
# plt.xlabel("k")
# plt.ylabel("y(k)")

# plt.show()