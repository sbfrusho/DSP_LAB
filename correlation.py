import numpy as np
import matplotlib.pyplot as plt

def _correlation(x, h):
    len_x = len(x)
    len_h = len(h)
    output_length = len_x + len_h - 1
    y = np.zeros(output_length)
    print(h)

    # for n in range (output_length):
    #     y_n = 0
    #     for k in range(len(x)):
    #         if 0 <= n-k < len(h):
    #             y_n += x[k] * h[n-k]
    #     y[n] = y_n
    # return y
    
    for k in range(output_length):
        y_k = 0
        for n in range(len_x):
            if 0 <= n - k + len_h - 1 < len_h:
                y_k += x[n] * h[n - k + len_h - 1]
        y[k] = y_k

    return y

# Input sequences
x = [1,2,3,4]
h = [1,2,3,4,5]
# h.reverse()

k = np.arange(len(x) + len(h) - 1)

# Compute cross-correlation
cross_correlation = _correlation(x, h)
correlate = np.correlate(x, h, mode='full')
print("Cross-correlation result:", cross_correlation)
print("Cross correlation using numpy:", correlate)

# # Plot the cross-correlation
# # plt.figure(figsize=(12,8))

# # plt.subplot(3,2,1)
# # plt.stem(k , cross_correlation)
# # plt.title("Correlation of x and h")
# # plt.xlabel("k")
# # plt.ylabel("y(k)")

# # plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# def _convolution(x , h):
#     result_length = len(x) + len(h) - 1
    
#     y = np.zeros(result_length)

#     for n in range (result_length):
#         y_n = 0
#         for k in range(len(x)):
#             if 0 <= n-k < len(h):
#                 y_n += x[k] * h[n-k]
#         y[n] = y_n
#     return y


# #define parameters
# x = [1,2,3,4,5]
# h = [1,2,3,4]
# h.reverse()

# convolution = _convolution(x,h)
# conovol = np.convolve(x,h)

# k = np.arange(len(x) + len(h) - 1)

# print(convolution)
# print(conovol)

# plt.figure(figsize=(12,8))

# plt.subplot(3,2,1)
# plt.stem(k , convolution)
# plt.title("Correlation of x and h")
# plt.xlabel("k")
# plt.ylabel("y(k)")

# plt.show()