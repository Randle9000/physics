"""
==================
Animated line plot
==================

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
# fig.set_size_inches(18.5, 10.5)
plt.ylim(-1, 1)

x = np.arange(0*np.pi, 2*np.pi, 0.1)
line, = ax.plot(x, np.sin(x), color='red', linewidth=2)
line2, = ax.plot(x, np.sin(x), color='blue', linewidth=1)
line3, = ax.plot(x, np.sin(x), color='green', linewidth=1)


def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    line2.set_ydata([np.nan] * len(x))
    line3.set_ydata([np.nan] * len(x))

    return [line]#, line2, line3


def animate(t):
    print(t)
    p = 24
    f1 = (np.sin(x-t/20)*np.cos(x/20))*np.cos(x-t/15)
    f2 = np.sin(x*p*3+t/4)
    f3 = np.cos(x*p/12-t/250)

    f =  f3*f2
    line.set_ydata(f) #*x/35)#*np.sin(x/5))
    line2.set_ydata(f3)
    line3.set_ydata(f2)
    return [line]#, line2, line3


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=20, blit=True, frames=200)# save_count=360)

# To save the animation, use e.g.

# ani.save("movie.mp4")

# or
#
# writer = animation.FFMpegWriter(
#     fps=60, metadata=dict(artist='Me'), bitrate=10000)
# ani.save("movie.mp4", writer=writer)
# ani.save('animation.gif', writer='imagemagick', fps=60)

plt.show()
