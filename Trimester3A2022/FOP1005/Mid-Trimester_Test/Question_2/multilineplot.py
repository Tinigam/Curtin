import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 8., 0.2)
t2 = t**2
t3 = t**0.4

plt.plot(t, t, 'r+', t, t2, 'go', t, t3, 'k^')
plt.title('Mid-Tri test Plotting')
plt.show()
