import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(["a", "b", "c", "d"], [1, 4, 9, 16])
ax.set_ylim(1, 16)
plt.show()