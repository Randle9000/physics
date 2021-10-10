import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc

# equivalent to rcParams['animation.html'] = 'html5'
# rc('animation', html='html5')

# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()

ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2, color='red')
line3, = ax.plot([], [], lw=2, color='green')
point, = ax.plot([], [], marker="o", markersize=7, color="purple")


def tracker_point(phi):
    x = 0.025
    x_p = 0.08/10*phi + x
    f1 = np.sin(2 * np.pi * (x * 10))
    f2 = np.sin(2 * np.pi * (x_p + 0.006 * phi))
    return np.array([x_p, f1*f2])


def init():
    line.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    point.set_data([], [])
    return (line3, point, line2, line)

# animation function. This is called sequentially

def animate(i):
    x = np.linspace(0, 2, 1000)
    f1 = np.sin(2 * np.pi * (x*10 - 0.08 * i))
    f2 = np.sin(2 * np.pi * (x + 0.006 * i))
    x_p, y_p = tracker_point(i)
    y = f1*f2

    line.set_data(x, f1)
    line2.set_data(x, f2)
    line3.set_data(x, y)
    point.set_data(x_p, y_p)

    return (line3, point,)


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=250, interval=50, blit=True)

plt.show()
