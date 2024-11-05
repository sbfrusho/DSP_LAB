import numpy as np
import matplotlib.pyplot as plt

f1 = 5
fs = 50
T = 1/fs

t = np.linspace(-1,1,1000)
xt = np.sin(2*np.pi*f1*t)
print(t , xt)
plt.figure(figsize=(12,8))
plt.subplot(3,2,1)
plt.plot(t,xt)
plt.show