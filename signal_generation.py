# import numpy as np
# import matplotlib.pyplot as plt

# def unit_step(n):
#     return np.where(n >= 0, 1, 0)

# def ramp_func(n):
#     return np.where(n >= 0, n, 0)

# def exponential_func(n, a):
#     return np.exp(a * n)

# def sin_signal(f1, t):
#     return np.sin(2 * np.pi * f1 * t)

# def cos_signal(f1, t):
#     return np.cos(2 * np.pi * f1 * t)

# f1 = 5
# fs = 20
# n = np.arange(-10, 10, 1)
# t = np.linspace(-1, 1, 1000)

# unit_signal = unit_step(n)
# ramp_signal = ramp_func(n)
# exponential_signal = exponential_func(n, 0.2)

# continuous_signal = sin_signal(f1, t)
# nts = np.arange(-1, 1, 1/fs)
# discrete_signal = sin_signal(f1, nts)

# plt.figure(figsize=(16, 10))

# plt.subplot(3, 2, 1)
# plt.stem(n, unit_signal)
# plt.title("Unit Step Signal")
# plt.xlabel("n")
# plt.ylabel("Amplitude")

# plt.subplot(3, 2, 2)
# plt.stem(n, ramp_signal)
# plt.title("Ramp Signal")
# plt.xlabel("n")
# plt.ylabel("Amplitude")

# plt.subplot(3, 2, 3)
# plt.stem(n, exponential_signal)
# plt.title("Exponential Signal")
# plt.xlabel("n")
# plt.ylabel("Amplitude")

# plt.subplot(3, 2, 4)
# plt.plot(t, continuous_signal, label="Continuous Sine", color="blue")
# plt.stem(nts, discrete_signal, linefmt="red", markerfmt="o", basefmt="black")
# plt.title("Continuous Sine Signal")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.legend()
# plt.grid(True)

# plt.subplot(3, 2, 5)
# plt.stem(nts, discrete_signal, linefmt="orange", markerfmt="o", basefmt="black")
# plt.title("Discrete Sine Signal")
# plt.xlabel("n (Discrete Time Samples)")
# plt.ylabel("Amplitude")
# plt.grid(True)

# fs = 8
# nts = np.arange(-1, 1, 1/fs)
# discrete_signal_alias = sin_signal(f1,nts)
# plt.subplot(3, 2, 6)
# plt.plot(t, continuous_signal, label="Continuous Sine", color="blue")
# plt.stem(nts, discrete_signal_alias, linefmt="red", markerfmt="o", basefmt="black")
# plt.title("Alias Sine Signal")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def unit_step_signal(n):
    return np.where(n >= 0 , 1 , 0)

def ramp_signal(n):
    return np.where(n >= 0 , n , 0)

def exponential_signal(a,n):
    return pow(a,n)

def sine_signal(f1 , t):
    return np.sin(2 * np.pi * f1 * t)

def cosine_signal(f1 , t):
    return np.cos(2 *np.pi * f1 * t)

#define parameters
n = np.arange(-10,10,1)

step_signal = unit_step_signal(n)
ramp = ramp_signal(n)
exponential = exponential_signal(1.5,n)

print(exponential)

plt.figure(figsize=(20,8))

plt.subplot(3,2,1)
plt.stem(n,step_signal)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.title("Unit Step Signal")

plt.subplot(3,2,2)
plt.stem(n,ramp)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.title("Unit Ramp Signal")

plt.subplot(3, 2, 3)
plt.stem(n, exponential)
plt.title("Exponential Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

plt.figure(figsize=(12,8))
#sine signal
f1 = 5

t = np.linspace(-1,1,1000)
xt = sine_signal(f1,t) #continuous signal

plt.subplot(3,2,1)
plt.plot(t,xt)
plt.title("Sine Wave")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

fs = 20 #nyquist rate
T = 1/fs
n = np.arange(-1,1,T)
xn = sine_signal(f1,n) #sampling with nyquist rate

plt.subplot(3,2,2)
plt.stem(n,xn)
plt.title("Sine Wave(sampling with nyquist rate)")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

fs = 50
T = 1/fs
n = np.arange(-1,1,T)
xn = sine_signal(f1,n) #up sampling

plt.subplot(3,2,3)
plt.stem(n,xn)
plt.title("Sine Wave(sampling with fs > 2 * fmax)")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

fs = 6
T = 1/fs
n = np.arange(-1,1,T)
xn = sine_signal(f1,n) #downsampling
plt.subplot(3,2,4)
plt.stem(n,xn)
plt.title("Sine Wave(sampling with fs < 2 * fmax)")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show() #sine ends here

plt.figure(figsize=(12,8))
#sine signal
f1 = 5

t = np.linspace(-1,1,1000)
xt = cosine_signal(f1,t) #continuous signal

plt.subplot(3,2,1)
plt.plot(t,xt)
plt.title("Cos Wave")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

fs = 20 #nyquist rate
T = 1/fs
n = np.arange(-1,1,T)
xn = cosine_signal(f1,n) #sampling with nyquist rate

plt.subplot(3,2,2)
plt.stem(n,xn)
plt.title("Cos Wave(sampling with nyquist rate)")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

fs = 50
T = 1/fs
n = np.arange(-1,1,T)
xn = cosine_signal(f1,n) #up sampling

plt.subplot(3,2,3)
plt.stem(n,xn)
plt.title("Cos Wave(sampling with fs > 2 * fmax)")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

fs = 6
T = 1/fs
n = np.arange(-1,1,T)
xn = cosine_signal(f1,n) #downsampling
plt.subplot(3,2,4)
plt.stem(n,xn)
plt.title("Cos Wave(sampling with fs < 2 * fmax)")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()



