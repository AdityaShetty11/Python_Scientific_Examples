# Gussian function

import numpy as np
import matplotlib.pyplot as plt

deviations = [1, 1.5, 2]
x = np.linspace(-5, 5, 100)

for sd in deviations:
    y = (1/(sd * np.sqrt(2*np.pi))) * np.exp(-x**2 / (2*sd**2))
    plt.plot(x, y)

plt.show()