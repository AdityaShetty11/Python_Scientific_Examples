import numpy as np
import matplotlib.pyplot as plt

# f1(x) = ln(1/cos(x)**2)
# f2(x) = ln(1/sin(x)**2)

n = np.linspace(-20, 20, 1001)

for i in range(1001):
    x = n
    y1 = np.log(1/np.sin(x)**2)
    y2 = np.log(1/np.cos(x)**2)

plt.plot(x,y1)
plt.plot(x,y2)


plt.show()