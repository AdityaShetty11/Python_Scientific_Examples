import numpy as np
import matplotlib.pyplot as pt
from matplotlib import pyplot as plt

t = np.linspace(0, 0.05, 1000)
k1 = 300
k2 = 100
A0 = 2.0
ksum = k1 + k2

A = A0 * np.exp(-ksum * t)
B = (k1 / ksum) * A0 * (1 - np.exp(-ksum * t))
C = (k2 / ksum) * A0 * (1 - np.exp(-ksum * t))

plt.plot(t,A)
plt.plot(t,B)
plt.plot(t,C)

plt.show()
