import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc

fig, ax = plt.subplots()

ax.set_xlim((0, 50))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,

# animation function. This is called sequentially

def animate(i):
    x = np.linspace(0, 50, 1000)
    y = np.sin(2 * np.pi * (np.sqrt(x) - 0.05 * i))
    line.set_data(x, y)
    return (line,)


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=500, interval=50, blit=True)

plt.show()
