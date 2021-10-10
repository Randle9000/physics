import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()

ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], lw=2)
point, = ax.plot([],[], lw=2, marker='o')

# initialization function: plot the background of each frame
def sinus_point(i):
    x_p = 0.01/11 * i
    # f1 = np.sin(4 * x - 0.01 * i)
    return np.array([x_p, 0])
def init():
    line.set_data([], [])
    point.set_data(0, 0)
    return (line, point,)

# animation function. This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(11 * x - 0.01 * i)
    x_p, y_p = sinus_point(i)
    line.set_data(x, y)
    point.set_data(x_p, y_p)

    return [line, point,]

# call the animator. blit=True means only re-draw the parts that
# have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=550, interval=2, blit=True)

plt.show()
